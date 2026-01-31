# Scripts Folder

## Purpose
Python scripts for automating Smartlead campaign management via API.

## Planned Scripts

### 1. create-campaign.py
**Purpose**: Create a new campaign in Smartlead

**Arguments**:
- `--name` - Campaign name
- `--from-email` - Sender email address
- `--from-name` - Sender display name
- `--sequence-file` - Path to email sequence template

**Usage**:
```bash
python scripts/create-campaign.py \
  --name "SaaS-CTO-Q1-2024" \
  --from-email "outreach@company.io" \
  --from-name "Sarah Chen" \
  --sequence-file "templates/sequences/cold-outreach.md"
```

**Output**:
- Campaign ID
- Dashboard URL
- Confirmation of email sequence upload

---

### 2. add-leads.py
**Purpose**: Upload and validate leads to existing campaign

**Arguments**:
- `--campaign-id` - Smartlead campaign ID
- `--lead-file` - Path to CSV file with leads
- `--validate-emails` - Optional flag to validate emails before upload

**CSV Format Required**:
```csv
email,first_name,last_name,company,title
john@example.com,John,Doe,Acme Inc,CTO
```

**Usage**:
```bash
python scripts/add-leads.py \
  --campaign-id "camp_abc123" \
  --lead-file "data/leads.csv" \
  --validate-emails
```

**Output**:
- Number of valid emails
- Number of invalid/duplicate emails removed
- Segmentation insights (if detected)

---

### 3. configure-campaign.py
**Purpose**: Set sending settings for campaign

**Arguments**:
- `--campaign-id` - Smartlead campaign ID
- `--daily-limit` - Max emails per day (default: 50)
- `--time-window` - Sending hours in recipient timezone (e.g., "8-17")
- `--days` - Days to send (e.g., "tue,wed,thu")
- `--enable-timezone-detection` - Auto-detect recipient timezone

**Usage**:
```bash
python scripts/configure-campaign.py \
  --campaign-id "camp_abc123" \
  --daily-limit 60 \
  --time-window "8-17" \
  --days "tue,wed,thu" \
  --enable-timezone-detection
```

**Output**:
- Confirmation of settings applied

---

### 4. send-test-email.py
**Purpose**: Send test email to verify campaign setup

**Arguments**:
- `--campaign-id` - Smartlead campaign ID
- `--test-email` - Email address to send test to

**Usage**:
```bash
python scripts/send-test-email.py \
  --campaign-id "camp_abc123" \
  --test-email "team@company.io"
```

**Output**:
- Confirmation test email sent
- Checklist of what to verify

---

### 5. activate-campaign.py
**Purpose**: Launch campaign and start sending

**Arguments**:
- `--campaign-id` - Smartlead campaign ID

**Usage**:
```bash
python scripts/activate-campaign.py --campaign-id "camp_abc123"
```

**Output**:
- Campaign status: Active
- Dashboard URL
- Estimated completion date
- Monitoring alerts configured

---

### 6. pause-campaign.py
**Purpose**: Emergency stop - pause active campaign

**Arguments**:
- `--campaign-id` - Smartlead campaign ID

**Usage**:
```bash
python scripts/pause-campaign.py --campaign-id "camp_abc123"
```

**Output**:
- Confirmation campaign paused
- Number of emails sent so far
- Number of leads remaining

---

### 7. get-campaign-metrics.py
**Purpose**: Fetch current campaign performance metrics

**Arguments**:
- `--campaign-id` - Smartlead campaign ID

**Usage**:
```bash
python scripts/get-campaign-metrics.py --campaign-id "camp_abc123"
```

**Output**:
```
Campaign: SaaS-CTO-Q1-2024
Status: Active
Emails sent: 120
Opens: 56 (46.7%)
Clicks: 15 (12.5%)
Replies: 6 (5.0%)
Meetings booked: 2 (1.7%)
Bounces: 1 (0.8%)
Spam: 0 (0%)
```

---

### 8. check-deliverability.py
**Purpose**: Monitor domain health and deliverability

**Arguments**:
- `--domain` - Sending domain to check

**Usage**:
```bash
python scripts/check-deliverability.py --domain "outreach.company.io"
```

**Output**:
- Domain reputation score
- Blacklist status
- SPF/DKIM/DMARC status
- Recent bounce rate
- Recent spam complaint rate

---

## Environment Variables

Create a `.env` file in this directory:

```env
SMARTLEAD_API_KEY=your_api_key_here
SMARTLEAD_API_URL=https://server.smartlead.ai/api/v1
```

**Security**: Never commit `.env` to version control!

---

## Dependencies

Create `requirements.txt`:

```
requests>=2.31.0
python-dotenv>=1.0.0
pandas>=2.0.0
validators>=0.20.0
```

Install with:
```bash
pip install -r requirements.txt
```

---

## Error Handling

All scripts should:
- ✅ Validate inputs before API calls
- ✅ Return clear error messages
- ✅ Exit with appropriate status codes
- ✅ Log API responses for debugging

---

## Testing

Before using in production:
1. Test with small lead lists (5-10 leads)
2. Send test emails to internal addresses
3. Verify all personalization tokens work
4. Check campaign appears correctly in Smartlead dashboard

---

## Notes

- These scripts will be called by Claude Code via the Bash tool
- Keep scripts simple and focused (one job per script)
- Add `--help` flag to all scripts for usage info
- Log all API calls for audit trail

---

## Future Scripts (Optional)

- `bulk-create-campaigns.py` - Create multiple campaigns at once
- `duplicate-campaign.py` - Clone existing campaign
- `update-sequence.py` - Modify email sequence mid-campaign
- `export-replies.py` - Export all replies to CSV
- `generate-report.py` - Create campaign performance report

---

## Integration with Claude Code

**How Claude uses these scripts**:

1. User requests: "Create a campaign called XYZ"
2. Claude invokes campaign-creator agent
3. Agent gathers required info (name, emails, etc.)
4. Agent executes: `python scripts/create-campaign.py --name "XYZ" ...`
5. Agent reports results to user

**Skills that use scripts**:
- `/launch-campaign` - Uses activate-campaign.py
- Campaign creator agent - Uses create-campaign.py, add-leads.py
- Monitoring workflows - Uses get-campaign-metrics.py

---

## Documentation

Each script should include:
- Docstring explaining purpose
- Argument descriptions
- Example usage
- Error handling notes

**Example structure**:
```python
#!/usr/bin/env python3
"""
create-campaign.py - Create new Smartlead campaign

Usage:
    python create-campaign.py --name "Campaign" --from-email "email@domain.com"

Returns:
    Campaign ID and dashboard URL on success
    Error message and exit code 1 on failure
"""

import argparse
import os
from dotenv import load_dotenv
import requests

# Script implementation here...
```

---

## Next Steps

1. Implement each script following this spec
2. Test with Smartlead API sandbox (if available)
3. Add error handling and validation
4. Document any API quirks or gotchas
5. Create integration tests

**TO DO**: Implement these scripts in next session
