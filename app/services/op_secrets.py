# noinspection PyPackageRequirements
from onepassword import Client


async def get_secret(onepassword_service_token: str, key: str) -> str:
    """
    Retrieves the password associated with the given key from 1Password using the service account.
    """
    client = await Client.authenticate(
        auth=onepassword_service_token,
        # Set the following to your own integration name and version.
        integration_name="Homelab API",
        integration_version="v1.0.0",
    )
    try:
        secret = await client.secrets.resolve(f"op://HomelabSecrets/{key}/password")
        return secret
    except Exception as e:
        return str(e)
