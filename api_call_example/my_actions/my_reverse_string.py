from asyncflows import Action, BaseModel, Field

import aiohttp


class Inputs(BaseModel):
    input_string: str


class Outputs(BaseModel):
    reversed_string: str

class MyReverseString(Action[Inputs, Outputs]):
    name = 'my_reverse_string'



class GetURL(Action[Inputs, Outputs]):
    name = "my_get_url"

    async def run(inputs: Inputs) -> Outputs:
     return Outputs(
        reversed_string=inputs.input_string[::-1]
    )
