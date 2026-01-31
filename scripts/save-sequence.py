#!/usr/bin/env python3
"""
save-sequence.py - Save email sequences to Smartlead campaign

Saves one or more email sequences to a campaign. Supports A/B testing variants.

Usage:
    python save-sequence.py --campaign-id CAMPAIGN_ID --sequence-file FILE

Arguments:
    --campaign-id       Campaign ID (required)
    --sequence-file     Path to JSON file with sequence data (required)

Sequence File Format (JSON):
    {
      "sequences": [
        {
          "seq_number": 1,
          "seq_delay_details": {"delay_in_days": 1},
          "variant_distribution_type": "MANUAL_EQUAL",
          "seq_variants": [
            {
              "subject": "Email subject",
              "email_body": "<p>HTML email body</p>",
              "variant_label": "A"
            }
          ]
        }
      ]
    }

Variant Distribution Types:
    - MANUAL_EQUAL: Equally distribute variants
    - MANUAL_PERCENTAGE: Specify % per variant
    - AI_EQUAL: AI picks winner based on metric

Environment Variables:
    SMARTLEAD_API_KEY    Your Smartlead API key

Returns:
    Success confirmation on success
    Error message and exit code 1 on failure

Example:
    python save-sequence.py --campaign-id "12345" --sequence-file sequences.json
"""

import argparse
import json
import os
import sys
from typing import Dict

try:
    import requests
    from dotenv import load_dotenv
except ImportError:
    print("Error: Required packages not installed.")
    print("Run: pip install requests python-dotenv")
    sys.exit(1)

# Load environment variables
load_dotenv()

# API Configuration
API_BASE_URL = "https://server.smartlead.ai/api/v1"
API_KEY = os.getenv("SMARTLEAD_API_KEY")


def load_sequence_file(file_path: str) -> Dict:
    """
    Load sequence data from JSON file.

    Args:
        file_path: Path to JSON file

    Returns:
        dict: Sequence data

    Raises:
        Exception: If file doesn't exist or is invalid JSON
    """
    if not os.path.exists(file_path):
        raise Exception(f"Sequence file not found: {file_path}")

    try:
        with open(file_path, 'r') as f:
            data = json.load(f)

        # Validate required structure
        if "sequences" not in data:
            raise ValueError("Sequence file must contain 'sequences' array")

        if not isinstance(data["sequences"], list):
            raise ValueError("'sequences' must be an array")

        if len(data["sequences"]) == 0:
            raise ValueError("'sequences' array cannot be empty")

        return data

    except json.JSONDecodeError as e:
        raise Exception(f"Invalid JSON in sequence file: {str(e)}")


def validate_sequence_data(sequences: list) -> None:
    """
    Validate sequence data structure.

    Args:
        sequences: List of sequence objects

    Raises:
        ValueError: If validation fails
    """
    valid_dist_types = ["MANUAL_EQUAL", "MANUAL_PERCENTAGE", "AI_EQUAL"]
    valid_metrics = ["OPEN_RATE", "CLICK_RATE", "REPLY_RATE", "POSITIVE_REPLY_RATE"]

    for idx, seq in enumerate(sequences):
        # Check required fields
        if "seq_number" not in seq:
            raise ValueError(f"Sequence {idx}: Missing 'seq_number'")

        if "seq_variants" not in seq:
            raise ValueError(f"Sequence {idx}: Missing 'seq_variants'")

        if len(seq["seq_variants"]) == 0:
            raise ValueError(f"Sequence {idx}: 'seq_variants' cannot be empty")

        # Validate distribution type if present
        if "variant_distribution_type" in seq:
            dist_type = seq["variant_distribution_type"]
            if dist_type not in valid_dist_types:
                raise ValueError(
                    f"Sequence {idx}: Invalid variant_distribution_type '{dist_type}'. "
                    f"Must be one of: {', '.join(valid_dist_types)}"
                )

            # Validate AI_EQUAL requirements
            if dist_type == "AI_EQUAL":
                if "winning_metric_property" not in seq:
                    raise ValueError(
                        f"Sequence {idx}: AI_EQUAL requires 'winning_metric_property'"
                    )

                metric = seq["winning_metric_property"]
                if metric not in valid_metrics:
                    raise ValueError(
                        f"Sequence {idx}: Invalid winning_metric_property '{metric}'. "
                        f"Must be one of: {', '.join(valid_metrics)}"
                    )

                if "lead_distribution_percentage" not in seq:
                    raise ValueError(
                        f"Sequence {idx}: AI_EQUAL requires 'lead_distribution_percentage'"
                    )

                pct = seq["lead_distribution_percentage"]
                if pct < 20 or pct > 100:
                    raise ValueError(
                        f"Sequence {idx}: lead_distribution_percentage must be 20-100"
                    )

            # Validate MANUAL_PERCENTAGE requirements
            if dist_type == "MANUAL_PERCENTAGE":
                total_pct = 0
                for variant in seq["seq_variants"][:10]:  # Only first 10 count
                    if "variant_distribution_percentage" not in variant:
                        raise ValueError(
                            f"Sequence {idx}: MANUAL_PERCENTAGE requires "
                            "'variant_distribution_percentage' on each variant"
                        )
                    total_pct += variant["variant_distribution_percentage"]

                if total_pct != 100:
                    raise ValueError(
                        f"Sequence {idx}: variant_distribution_percentage must total 100% "
                        f"(currently {total_pct}%)"
                    )

        # Validate each variant
        for v_idx, variant in enumerate(seq["seq_variants"]):
            if "subject" not in variant:
                raise ValueError(
                    f"Sequence {idx}, Variant {v_idx}: Missing 'subject'"
                )

            if "email_body" not in variant:
                raise ValueError(
                    f"Sequence {idx}, Variant {v_idx}: Missing 'email_body'"
                )

            if "variant_label" not in variant:
                raise ValueError(
                    f"Sequence {idx}, Variant {v_idx}: Missing 'variant_label'"
                )


def save_campaign_sequence(campaign_id: str, sequence_data: Dict) -> dict:
    """
    Save sequences to campaign.

    Args:
        campaign_id: Campaign ID
        sequence_data: Sequence data dict with 'sequences' array

    Returns:
        dict: API response

    Raises:
        Exception: If API request fails
    """
    if not API_KEY:
        raise Exception("SMARTLEAD_API_KEY environment variable not set")

    # Validate sequence data
    validate_sequence_data(sequence_data["sequences"])

    endpoint = f"{API_BASE_URL}/campaigns/{campaign_id}/sequences"

    params = {
        "api_key": API_KEY
    }

    try:
        num_sequences = len(sequence_data["sequences"])
        print(f"Saving {num_sequences} sequence(s) to campaign {campaign_id}...")

        for seq in sequence_data["sequences"]:
            num_variants = len(seq["seq_variants"])
            dist_type = seq.get("variant_distribution_type", "MANUAL_EQUAL")
            print(f"  Sequence {seq['seq_number']}: {num_variants} variant(s) ({dist_type})")

        response = requests.post(
            endpoint,
            params=params,
            json=sequence_data,
            headers={"Content-Type": "application/json"},
            timeout=30
        )

        # Check if request was successful
        response.raise_for_status()

        result = response.json()
        return result

    except requests.exceptions.HTTPError as e:
        error_msg = f"HTTP Error: {e.response.status_code}"
        try:
            error_detail = e.response.json()
            error_msg += f"\nDetails: {json.dumps(error_detail, indent=2)}"
        except:
            error_msg += f"\nResponse: {e.response.text}"
        raise Exception(error_msg)

    except requests.exceptions.Timeout:
        raise Exception("Request timed out. Please try again.")

    except requests.exceptions.RequestException as e:
        raise Exception(f"Request failed: {str(e)}")


def main():
    parser = argparse.ArgumentParser(
        description="Save email sequences to Smartlead campaign",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Example Sequence File (sequences.json):
{
  "sequences": [
    {
      "seq_number": 1,
      "seq_delay_details": {"delay_in_days": 0},
      "variant_distribution_type": "MANUAL_EQUAL",
      "seq_variants": [
        {
          "subject": "Quick question about {{company}}",
          "email_body": "<p>Hi {{first_name}},<br><br>Quick question...</p>",
          "variant_label": "A"
        },
        {
          "subject": "{{first_name}}, quick question",
          "email_body": "<p>Hi {{first_name}},<br><br>Different approach...</p>",
          "variant_label": "B"
        }
      ]
    },
    {
      "seq_number": 2,
      "seq_delay_details": {"delay_in_days": 3},
      "variant_distribution_type": "MANUAL_EQUAL",
      "seq_variants": [
        {
          "subject": "Following up",
          "email_body": "<p>Hi {{first_name}},<br><br>Following up...</p>",
          "variant_label": "A"
        }
      ]
    }
  ]
}

Variant Distribution Types:
  MANUAL_EQUAL       - Equal distribution across variants
  MANUAL_PERCENTAGE  - Specify % per variant (must total 100%)
  AI_EQUAL          - AI picks winner based on metric

For AI_EQUAL, also include:
  "winning_metric_property": "REPLY_RATE",
  "lead_distribution_percentage": 40

Environment Variables:
  SMARTLEAD_API_KEY    Your Smartlead API key (required)
        """
    )

    parser.add_argument(
        "--campaign-id",
        required=True,
        help="Campaign ID"
    )

    parser.add_argument(
        "--sequence-file",
        required=True,
        help="Path to JSON file with sequence data"
    )

    args = parser.parse_args()

    try:
        # Load sequence file
        sequence_data = load_sequence_file(args.sequence_file)

        # Save sequences
        result = save_campaign_sequence(args.campaign_id, sequence_data)

        # Success output
        print("\n" + "="*60)
        print("✓ Sequences Saved Successfully!")
        print("="*60)
        print(f"Campaign ID: {args.campaign_id}")
        print(f"Sequences: {len(sequence_data['sequences'])}")

        # Show summary
        for seq in sequence_data["sequences"]:
            variants = len(seq["seq_variants"])
            delay = seq.get("seq_delay_details", {}).get("delay_in_days", 0)
            dist_type = seq.get("variant_distribution_type", "MANUAL_EQUAL")

            print(f"\n  Email {seq['seq_number']}:")
            print(f"    Delay: {delay} day(s)")
            print(f"    Variants: {variants}")
            print(f"    Distribution: {dist_type}")

            if dist_type == "AI_EQUAL":
                metric = seq.get("winning_metric_property", "N/A")
                pct = seq.get("lead_distribution_percentage", "N/A")
                print(f"    Winning Metric: {metric}")
                print(f"    Test Size: {pct}% of leads")

        print("="*60)

        print("\nNext Steps:")
        print("1. Upload leads to campaign")
        print("2. Send test email")
        print("3. Activate campaign")

        # Return success
        sys.exit(0)

    except Exception as e:
        print(f"\n✗ Error: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
