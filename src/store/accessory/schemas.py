from pydantic import BaseModel, ConfigDict, conint

from store.utils.generators import camel_case_generator


class AccessoryBase(BaseModel):
    name: str
    price: int
    description: str | None
    quantity: conint(ge=0)
    images: list[str]

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=camel_case_generator
    )


class Accessory(AccessoryBase):
    id: int


class AccessoryCreate(AccessoryBase):
    pass


class AccessoryUpdate(AccessoryBase):
    pass
