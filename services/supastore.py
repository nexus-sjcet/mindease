import supabase

filepath = "images/primetime.jpg"
with open(filepath, "rb") as f:
    supabase.storage.from_("graph").upload(
        file=f, path=path_on_supastorage, file_options={"content-type": "audio/mpeg"}
    )
