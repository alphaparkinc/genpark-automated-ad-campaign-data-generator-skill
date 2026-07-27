class AutomatedAdCampaignDataGeneratorClient:
    def generate_ad_campaigns(self, product_analytics: dict, target_channels: list) -> dict:
        camps = []
        for ch in target_channels:
            camps.append({
                "channel": ch,
                "headline": f"Boost Efficiency by 3x with {product_analytics.get('name', 'Our Product')}",
                "cta": "Start Free Trial Today",
                "target_segment": "B2B SaaS Executives"
            })
        return {
            "generated_campaigns": camps,
            "estimated_ctr": 4.85
        }
