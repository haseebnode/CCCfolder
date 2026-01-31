#!/usr/bin/env python3
"""
create-campaign.py - Create new Smartlead campaign

Creates a new campaign in Smartlead with the specified name.

Usage:
    python create-campaign.py --name "Campaign Name" [--client-id CLIENT_ID]

Arguments:
    --name          Campaign name (required)
    --client-id     Client ID (optional, leave null for main account)

Environment Variables:
    SMARTLEAD_API_KEY    Your Smartlead API key

Returns:
    Campaign ID and success message on success
    Error message and exit code 1 on failure

Example:
    python create-campaign.py --name "SaaS-CTO-Q1-2024"
    python create-campaign.py --name "Client Campaign" --client-id 22
"""

import argparse
import json
import os
import sys
from typing import Optional

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


def create_campaign(name: str, client_id: Optional[int] = None) -> dict:
    """
    Create a new campaign in Smartlead.

    Args:
        name: Campaign name
        client_id: Optional client ID (None for main account)

    Returns:
        dict: API response containing campaign details

    Raises:
        Exception: If API request fails
    """
    if not API_KEY:
        raise Exception("SMARTLEAD_API_KEY environment variable not set")

    endpoint = f"{API_BASE_URL}/campaigns/create"

    params = {
        "api_key": API_KEY
    }

    payload = {
        "name": name
    }

    # Only include client_id if provided
    if client_id is not None:
        payload["client_id"] = client_id

    try:
        print(f"Creating campaign: '{name}'...")

        response = requests.post(
            endpoint,
            params=params,
            json=payload,
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
        description="Create a new campaign in Smartlead",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python create-campaign.py --name "SaaS-CTO-Q1-2024"
  python create-campaign.py --name "Client Campaign" --client-id 22

Environment Variables:
  SMARTLEAD_API_KEY    Your Smartlead API key (required)
        """
    )

    parser.add_argument(
        "--name",
        required=True,
        help="Campaign name"
    )

    parser.add_argument(
        "--client-id",
        type=int,
        help="Client ID (optional, leave empty for main account)"
    )

    args = parser.parse_args()

    try:
        # Create campaign
        result = create_campaign(
            name=args.name,
            client_id=args.client_id
        )

        # Extract campaign details
        campaign_id = result.get("id")
        campaign_name = result.get("name")

        # Success output
        print("\n" + "="*60)
        print("✓ Campaign Created Successfully!")
        print("="*60)
        print(f"Campaign ID: {campaign_id}")
        print(f"Campaign Name: {campaign_name}")
        print(f"Dashboard: https://app.smartlead.ai/campaigns/{campaign_id}")
        print("="*60)

        print("\nNext Steps:")
        print("1. Configure campaign schedule")
        print("2. Add email sequences")
        print("3. Upload leads")
        print("4. Activate campaign")

        # Return success
        sys.exit(0)

    except Exception as e:
        print(f"\n✗ Error: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
