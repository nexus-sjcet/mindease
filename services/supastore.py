from supabase import create_client, Client
from dotenv import load_dotenv
import os


def upload(filename):
    load_dotenv()

    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")
    supabase: Client = create_client(url, key)

    filepath = f"images/{filename}.png"

    with open(filepath, "rb") as file:
        supabase.storage.from_("graph-bucket").upload(
            file=file,
            path=f"{filename}.png",
            file_options={"content-type": "image/png"},
        )

        return supabase.storage.from_("graph-bucket").get_public_url(f"{filename}.png")
