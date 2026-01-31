#!/usr/bin/env python3
"""
configure-campaign.py - Configure Smartlead campaign sending schedule

Updates campaign schedule settings including timezone, days, hours, and limits.

Usage:
    python configure-campaign.py --campaign-id CAMPAIGN_ID [OPTIONS]

Arguments:
    --campaign-id           Campaign ID (required)
    --timezone              Timezone (default: America/Los_Angeles)
    --days                  Days of week as comma-separated numbers 0-6 (default: 1,2,3,4)
    --start-hour            Start hour in 24h format HH:MM (default: 09:00)
    --end-hour              End hour in 24h format HH:MM (default: 17:00)
    --daily-limit           Max new leads per day (default: 50)
    --min-delay             Min minutes between emails (default: 10)
    --start-date            Campaign start date ISO format (optional)

Environment Variables:
    SMARTLEAD_API_KEY    Your Smartlead API key

Returns:
    Success confirmation on success
    Error message and exit code 1 on failure

Example:
    python configure-campaign.py --campaign-id "12345" --daily-limit 60
    python configure-campaign.py --campaign-id "12345" --timezone "America/New_York" --days "1,2,3" --start-hour "08:00" --end-hour "18:00"
"""

import argparse
import json
import os
import sys
from datetime import datetime
from typing import List, Optional

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

# Timezone reference: https://help.smartlead.ai/Timezones-20fcff9ddbb5441790c7c8e5ce0e9233


def parse_days(days_str: str) -> List[int]:
    """
    Parse comma-separated day numbers.

    Args:
        days_str: Comma-separated numbers like "0,1,2,3,4,5,6"

    Returns:
        List of integers
    """
    try:
        days = [int(d.strip()) for d in days_str.split(",")]

        # Validate days are 0-6
        for day in days:
            if day < 0 or day > 6:
                raise ValueError(f"Invalid day: {day}. Days must be 0-6 (0=Sunday, 6=Saturday)")

        return days
    except ValueError as e:
        raise ValueError(f"Invalid days format: {str(e)}")


def validate_time_format(time_str: str) -> str:
    """
    Validate time is in HH:MM format.

    Args:
        time_str: Time string like "09:00"

    Returns:
        Validated time string
    """
    try:
        datetime.strptime(time_str, "%H:%M")
        return time_str
    except ValueError:
        raise ValueError(f"Invalid time format: {time_str}. Use HH:MM (e.g., 09:00)")


def configure_campaign_schedule(
    campaign_id: str,
    timezone: str = "America/Los_Angeles",
    days_of_week: List[int] = None,
    start_hour: str = "09:00",
    end_hour: str = "17:00",
    daily_limit: int = 50,
    min_delay: int = 10,
    start_date: Optional[str] = None
) -> dict:
    """
    Configure campaign schedule settings.

    Args:
        campaign_id: Campaign ID
        timezone: Timezone string
        days_of_week: List of day numbers (0=Sunday, 6=Saturday)
        start_hour: Start hour in HH:MM format
        end_hour: End hour in HH:MM format
        daily_limit: Max new leads per day
        min_delay: Min minutes between emails
        start_date: Optional campaign start date (ISO format)

    Returns:
        dict: API response

    Raises:
        Exception: If API request fails
    """
    if not API_KEY:
        raise Exception("SMARTLEAD_API_KEY environment variable not set")

    if days_of_week is None:
        days_of_week = [1, 2, 3, 4]  # Mon-Thu default

    # Validate time formats
    validate_time_format(start_hour)
    validate_time_format(end_hour)

    endpoint = f"{API_BASE_URL}/campaigns/{campaign_id}/schedule"

    params = {
        "api_key": API_KEY
    }

    payload = {
        "timezone": timezone,
        "days_of_the_week": days_of_week,
        "start_hour": start_hour,
        "end_hour": end_hour,
        "min_time_btw_emails": min_delay,
        "max_new_leads_per_day": daily_limit
    }

    # Add start date if provided
    if start_date:
        payload["schedule_start_time"] = start_date

    try:
        print(f"Configuring campaign schedule for campaign ID: {campaign_id}...")
        print(f"  Timezone: {timezone}")
        print(f"  Days: {days_of_week} (0=Sun, 6=Sat)")
        print(f"  Hours: {start_hour} - {end_hour}")
        print(f"  Daily limit: {daily_limit} leads")
        print(f"  Min delay: {min_delay} minutes")

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
        description="Configure Smartlead campaign schedule settings",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic configuration with daily limit
  python configure-campaign.py --campaign-id "12345" --daily-limit 60

  # Full configuration
  python configure-campaign.py \\
    --campaign-id "12345" \\
    --timezone "America/New_York" \\
    --days "1,2,3" \\
    --start-hour "08:00" \\
    --end-hour "18:00" \\
    --daily-limit 100 \\
    --min-delay 15

  # Conservative settings for new domain
  python configure-campaign.py \\
    --campaign-id "12345" \\
    --daily-limit 30 \\
    --days "1,2,3,4"

Days of Week:
  0 = Sunday, 1 = Monday, 2 = Tuesday, 3 = Wednesday
  4 = Thursday, 5 = Friday, 6 = Saturday

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
        "--timezone",
        default="America/Los_Angeles",
        help="Timezone (default: America/Los_Angeles). See: https://help.smartlead.ai/Timezones"
    )

    parser.add_argument(
        "--days",
        default="1,2,3,4",
        help="Days of week as comma-separated numbers 0-6 (default: 1,2,3,4 = Mon-Thu)"
    )

    parser.add_argument(
        "--start-hour",
        default="09:00",
        help="Start hour in 24h format HH:MM (default: 09:00)"
    )

    parser.add_argument(
        "--end-hour",
        default="17:00",
        help="End hour in 24h format HH:MM (default: 17:00)"
    )

    parser.add_argument(
        "--daily-limit",
        type=int,
        default=50,
        help="Max new leads per day (default: 50)"
    )

    parser.add_argument(
        "--min-delay",
        type=int,
        default=10,
        help="Min minutes between emails (default: 10)"
    )

    parser.add_argument(
        "--start-date",
        help="Campaign start date in ISO format (e.g., 2024-01-31T09:00:00Z)"
    )

    args = parser.parse_args()

    try:
        # Parse days
        days_of_week = parse_days(args.days)

        # Configure campaign
        result = configure_campaign_schedule(
            campaign_id=args.campaign_id,
            timezone=args.timezone,
            days_of_week=days_of_week,
            start_hour=args.start_hour,
            end_hour=args.end_hour,
            daily_limit=args.daily_limit,
            min_delay=args.min_delay,
            start_date=args.start_date
        )

        # Success output
        print("\n" + "="*60)
        print("✓ Campaign Schedule Configured Successfully!")
        print("="*60)
        print(f"Campaign ID: {args.campaign_id}")
        print(f"Settings applied:")
        print(f"  • Timezone: {args.timezone}")
        print(f"  • Active days: {days_of_week}")
        print(f"  • Sending hours: {args.start_hour} - {args.end_hour}")
        print(f"  • Daily limit: {args.daily_limit} leads/day")
        print(f"  • Min delay: {args.min_delay} minutes")
        print("="*60)

        print("\nNext Steps:")
        print("1. Add email sequences to campaign")
        print("2. Upload leads")
        print("3. Send test email")
        print("4. Activate campaign")

        # Return success
        sys.exit(0)

    except Exception as e:
        print(f"\n✗ Error: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
