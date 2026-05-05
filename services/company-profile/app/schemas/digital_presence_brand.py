from pydantic import BaseModel


class DigitalPresenceBrandBase(BaseModel):
    quality_of_website: str | None
    awards_recognition: str | None
    brand_sentiment_score: str | None
    news_about_company: str | None
    average_deal_size: str | None
    top_customers: str | None
    website_traffic_rank: str | None
    social_media_followers_combined: str | None
    glassdoor_rating: str | None
    indeed_rating: str | None
    google_reviews_rating: str | None


class DigitalPresenceBrandCreateUpdate(DigitalPresenceBrandBase):
    pass
