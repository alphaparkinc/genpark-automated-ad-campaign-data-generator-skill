from client import AutomatedAdCampaignDataGeneratorClient

def main():
    client = AutomatedAdCampaignDataGeneratorClient()
    res = client.generate_ad_campaigns({"name": "GenPark AI Platform"}, ["Google Ads", "LinkedIn Ads"])
    print(f"Estimated CTR: {res['estimated_ctr']}%")
    print("Generated Campaigns:")
    for c in res["generated_campaigns"]:
        print(f"  [{c['channel']}] Headline: '{c['headline']}' | CTA: '{c['cta']}'")

if __name__ == "__main__":
    main()
