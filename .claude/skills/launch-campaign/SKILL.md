---
name: launch-campaign
description: Launches a complete Smartlead campaign with leads and tracking. Manual invocation only.
argument-hint: [campaign-name]
disable-model-invocation: true
allowed-tools: Bash, Read
---

Launch Smartlead campaign: $ARGUMENTS

**Pre-Launch Checklist**
1. Verify campaign exists in Smartlead
2. Email copy is approved
3. Lead list is prepared and segmented
4. Sending domain is warmed up
5. Tracking parameters are configured

**Launch Steps**

1. **Upload Leads**
   ```bash
   python scripts/add-leads.py "$0" "path/to/leads.csv"
   ```

2. **Configure Settings**
   - Set daily sending limits (based on domain age)
   - Configure time windows (recipient timezone)
   - Enable link tracking
   - Set up reply detection

3. **Final Verification**
   - Send test email to internal address
   - Verify all personalization tokens work
   - Check unsubscribe link functions
   - Confirm deliverability settings

4. **Activate Campaign**
   ```bash
   python scripts/activate-campaign.py "$0"
   ```

5. **Post-Launch**
   - Provide campaign dashboard URL
   - Set monitoring alerts for bounce rate
   - Schedule 24-hour performance review
   - Document campaign in /examples/

**Emergency Stop**: If issues detected, run:
```bash
python scripts/pause-campaign.py "$0"
```
