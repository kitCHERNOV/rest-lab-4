from pydantic import BaseModel, Field

class CurrencyExchange(BaseModel):
    from_currency: str = Field(..., title="Код валюты, которую вы хотите обменять")
    to_currency: str = Field(..., title="Код валюты, на которую вы хотите обменять")
    amount: float = Field(1.0, title="Количество для обмена", gt=0)