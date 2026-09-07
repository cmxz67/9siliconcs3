class Cellphone:

    def __init__(self, model, apps, storage, limit):
        self.model = model
        self.apps = apps
        self.storage = storage
        self.__limit = limit

    def download(self, app):
        self.apps.append(app)
        print(app, "was downloaded.")

    def open_app(self, app):
        print("Opening", app)

    def show_storage(self):
        print("Storage:", self.storage, "GB")

    def get_limit(self):
        return self.__limit


phone1 = Cellphone(
    "Samsung A15",
    ["YouTube", "Messenger"],
    64,
    128
)

phone2 = Cellphone(
    "Samsung A06",
    ["Spotify", "Facebook"],
    32,
    64
)


print("--- BEFORE ---")

print("PHONE 1")
print("Model:", phone1.model)
print("Apps:", phone1.apps)
phone1.show_storage()

print()

print("PHONE 2")
print("Model:", phone2.model)
print("Apps:", phone2.apps)
phone2.show_storage()


print("\nDownloading Roblox on Phone 1...")
phone1.download("Roblox")


print("\n--- AFTER ---")

print("PHONE 1")
print("Apps:", phone1.apps)
phone1.show_storage()

print()

print("PHONE 2")
print("Apps:", phone2.apps)
phone2.show_storage()