import asyncio

from permit import Permit
from fastapi import FastAPI, status, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()



permit = Permit(  # in production, you might need to change this url to fit your deployment
    pdp="https://cloudpdp.api.permit.io",  # your api key
    token="permit_key_abJZxRNEdcDSFqSWpmsdgyKzlbuCzHS2LLhbSB9uyTNc8G0Lvlo0MMZATbx5DshtOP4lh9CEXDEMBZLZnnxlXF",
)

# This user was defined by you in the previous step and

# is already assigned with a role in the permission system.

user = {
    "id": "7541",
    "firstName": "Aditya",
    "lastName": "Singhania",
    "email": "aditya.singhania@example.com",
}  # in a real app, you would typically decode the user id from a JWT token


@app.get("/")
async def check_permissions():  # After we created this user in the previous step, we also synced the user's identifier # to permit.io servers with permit.write(permit.api.syncUser(user)). The user identifier # can be anything (email, db id, etc) but must be unique for each user. Now that the # user is synced, we can use its identifier to check permissions with 'permit.check()'.
    permitted = await permit.check(user["id"], "create", "location_acess_feature")
    if not permitted:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail={
            "result": f"{user.get('firstName')} {user.get('lastName')} is NOT PERMITTED to read document!"
        })

    return JSONResponse(status_code=status.HTTP_200_OK, content={
        "result": f"{user.get('firstName')} {user.get('lastName')} is PERMITTED to read document!"
    })