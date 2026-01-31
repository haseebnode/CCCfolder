# Smartlead Scripts Setup Guide

## Quick Start

### 1. Install Dependencies

```bash
cd scripts/
pip install -r requirements.txt
```

### 2. Configure API Key

Copy the example environment file and add your API key:

```bash
cp .env.example .env
```

Edit `.env` and add your Smartlead API key:

```env
SMARTLEAD_API_KEY=your_actual_api_key_here
```

**Get your API key**: https://app.smartlead.ai/app/settings/integrations

**⚠️ IMPORTANT**: Never commit `.env` to version control!

### 3. Test Your Setup

Create a test campaign:

```bash
python create-campaign.py --name "Test Campaign"
```

If successful, you'll see:
```
✓ Campaign Created Successfully!
Campaign ID: 12345
Dashboard: https://app.smartlead.ai/campaigns/12345
```

---

## Available Scripts

### 1. create-campaign.py

Creates a new campaign in Smartlead.

**Basic usage**:
```bash
python create-campaign.py --name "My Campaign"
```

**With client ID**:
```bash
python create-campaign.py --name "Client Campaign" --client-id 22
```

**What it returns**:
- Campaign ID
- Campaign name
- Dashboard URL

---

### 2. configure-campaign.py

Configures campaign sending schedule.

**Basic usage** (50 leads/day, Mon-Thu, 9am-5pm):
```bash
python configure-campaign.py --campaign-id "12345" --daily-limit 50
```

**Full customization**:
```bash
python configure-campaign.py \
  --campaign-id "12345" \
  --timezone "America/New_York" \
  --days "1,2,3" \
  --start-hour "08:00" \
  --end-hour "18:00" \
  --daily-limit 100 \
  --min-delay 15
```

**Conservative settings** (new domain):
```bash
python configure-campaign.py \
  --campaign-id "12345" \
  --daily-limit 30 \
  --days "1,2,3,4"
```

**Parameters**:
- `--timezone`: Timezone string (see: https://help.smartlead.ai/Timezones)
- `--days`: Comma-separated days (0=Sun, 1=Mon, ..., 6=Sat)
- `--start-hour`: Start sending hour (24h format, HH:MM)
- `--end-hour`: Stop sending hour (24h format, HH:MM)
- `--daily-limit`: Max new leads per day
- `--min-delay`: Minimum minutes between emails

---

### 3. save-sequence.py

Saves email sequences to a campaign.

**Usage**:
```bash
python save-sequence.py \
  --campaign-id "12345" \
  --sequence-file "example-sequence.json"
```

**Sequence file format** (see `example-sequence.json`):
```json
{
  "sequences": [
    {
      "seq_number": 1,
      "seq_delay_details": {"delay_in_days": 0},
      "variant_distribution_type": "MANUAL_EQUAL",
      "seq_variants": [
        {
          "subject": "Subject line",
          "email_body": "<p>HTML email body</p>",
          "variant_label": "A"
        }
      ]
    }
  ]
}
```

**Personalization tokens** you can use:
- `{{first_name}}`
- `{{last_name}}`
- `{{company}}`
- `{{job_title}}`
- Any custom field from your lead list

**Variant distribution types**:
- `MANUAL_EQUAL`: Equal split across variants
- `MANUAL_PERCENTAGE`: Specify % per variant (must total 100%)
- `AI_EQUAL`: AI selects winner based on metric

**For AI_EQUAL**, also include:
```json
{
  "variant_distribution_type": "AI_EQUAL",
  "winning_metric_property": "REPLY_RATE",
  "lead_distribution_percentage": 40
}
```

**Metrics**:
- `OPEN_RATE`
- `CLICK_RATE`
- `REPLY_RATE`
- `POSITIVE_REPLY_RATE`

---

## Complete Workflow Example

### Step 1: Create Campaign
```bash
python create-campaign.py --name "SaaS-CTO-Q1-2024"
```

**Output**:
```
✓ Campaign Created Successfully!
Campaign ID: 12345
```

---

### Step 2: Configure Schedule
```bash
python configure-campaign.py \
  --campaign-id "12345" \
  --timezone "America/New_York" \
  --days "1,2,3,4" \
  --start-hour "09:00" \
  --end-hour "17:00" \
  --daily-limit 60 \
  --min-delay 10
```

**Output**:
```
✓ Campaign Schedule Configured Successfully!
Settings applied:
  • Timezone: America/New_York
  • Active days: [1, 2, 3, 4]
  • Sending hours: 09:00 - 17:00
  • Daily limit: 60 leads/day
  • Min delay: 10 minutes
```

---

### Step 3: Add Email Sequences
```bash
python save-sequence.py \
  --campaign-id "12345" \
  --sequence-file "my-sequences.json"
```

**Output**:
```
✓ Sequences Saved Successfully!
Campaign ID: 12345
Sequences: 3

  Email 1:
    Delay: 0 day(s)
    Variants: 2
    Distribution: MANUAL_EQUAL

  Email 2:
    Delay: 3 day(s)
    Variants: 1
    Distribution: MANUAL_EQUAL

  Email 3:
    Delay: 4 day(s)
    Variants: 1
    Distribution: MANUAL_EQUAL
```

---

### Step 4: Upload Leads

**Note**: Lead upload script not yet implemented. For now, upload via:
- Smartlead dashboard: https://app.smartlead.ai/campaigns/12345
- Or implement `add-leads.py` using the API endpoint:
  - POST `/api/v1/campaigns/{campaign-id}/leads`

---

### Step 5: Activate Campaign

**Note**: Activation script not yet implemented. For now:
1. Go to campaign dashboard
2. Send test email to verify everything works
3. Click "Activate" button

Or implement `activate-campaign.py` using:
- PATCH `/api/v1/campaigns/{campaign-id}/status`

---

## Recommended Settings by Domain Age

### New Domain (< 3 months)
```bash
python configure-campaign.py \
  --campaign-id "12345" \
  --daily-limit 30 \
  --days "1,2,3,4" \
  --start-hour "09:00" \
  --end-hour "17:00" \
  --min-delay 15
```

### Warmed Domain (3-6 months)
```bash
python configure-campaign.py \
  --campaign-id "12345" \
  --daily-limit 60 \
  --days "1,2,3,4" \
  --start-hour "08:00" \
  --end-hour "18:00" \
  --min-delay 10
```

### Aged Domain (6+ months)
```bash
python configure-campaign.py \
  --campaign-id "12345" \
  --daily-limit 100 \
  --days "1,2,3,4,5" \
  --start-hour "08:00" \
  --end-hour "18:00" \
  --min-delay 10
```

---

## Troubleshooting

### Error: "SMARTLEAD_API_KEY environment variable not set"

**Solution**: Make sure you created `.env` file with your API key:
```bash
cp .env.example .env
# Edit .env and add your key
```

### Error: "Module not found: requests"

**Solution**: Install dependencies:
```bash
pip install -r requirements.txt
```

### Error: "HTTP Error: 401"

**Solution**: Your API key is invalid. Get a new one from:
https://app.smartlead.ai/app/settings/integrations

### Error: "HTTP Error: 404" (campaign not found)

**Solution**: Check the campaign ID is correct. List campaigns via API or dashboard.

### Error: "Invalid time format"

**Solution**: Use 24-hour format with colon: `09:00`, not `9:00` or `09:00am`

---

## Testing Before Production

Before using with real campaigns:

1. **Create test campaign**:
   ```bash
   python create-campaign.py --name "TEST - Delete Me"
   ```

2. **Configure conservatively**:
   ```bash
   python configure-campaign.py --campaign-id "12345" --daily-limit 5
   ```

3. **Use test sequence**:
   - Create `test-sequence.json` with one simple email
   - Save it to campaign
   - Upload 5 test leads (internal email addresses)

4. **Verify in dashboard**:
   - Check campaign appears correctly
   - Review sequence timing
   - Send test email to yourself

5. **Delete test campaign** when done

---

## Integration with Claude Code

These scripts are designed to be called by Claude Code agents and skills.

**Example from campaign-creator agent**:
```python
# Claude executes via Bash tool
python scripts/create-campaign.py --name "User's Campaign"
```

**Example from /launch-campaign skill**:
```bash
python scripts/configure-campaign.py --campaign-id "$0" --daily-limit 60
python scripts/save-sequence.py --campaign-id "$0" --sequence-file "sequences.json"
```

See agent and skill files in `.claude/` for integration examples.

---

## Next Scripts to Implement

Priority scripts still needed:

1. **add-leads.py** - Upload CSV of leads
2. **activate-campaign.py** - Start campaign sending
3. **get-metrics.py** - Fetch campaign performance
4. **pause-campaign.py** - Emergency stop

See `README.md` for specifications of these scripts.

---

## Security Notes

- ✅ Never commit `.env` to version control
- ✅ Keep API keys secret
- ✅ Use environment variables, not hardcoded keys
- ✅ Rotate API keys regularly
- ✅ Limit API key permissions if possible

---

## Getting Help

**Script help**:
```bash
python create-campaign.py --help
python configure-campaign.py --help
python save-sequence.py --help
```

**Smartlead API docs**:
https://server.smartlead.ai/docs

**Timezone list**:
https://help.smartlead.ai/Timezones-20fcff9ddbb5441790c7c8e5ce0e9233

**Issues?**
- Check error messages carefully
- Verify API key is valid
- Test with small campaigns first
- Review Smartlead dashboard for details
