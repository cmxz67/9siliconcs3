class App:

    def __init__(self, name, category):
        self.name = name
        self.category = category


class Cellphone:

    def __init__(self, model, apps, storage, limit):
        self.model = model
        self.apps = apps
        self.storage = storage
        self.__limit = limit

    def add_app(self, app):
        self.apps.append(app)
        print(app.name, "was added to", self.model)

    def show_apps(self):
        for app in self.apps:
            print("App:", app.name)
            print("Category:", app.category)

    def show_storage(self):
        print("Storage:", self.storage, "GB")

    def get_limit(self):
        return self.__limit



phone1 = Cellphone(
    "Samsung A15",
    [],
    64,
    128
)


phone2 = Cellphone(
    "Samsung A06",
    [],
    32,
    64
)



youtube = App("YouTube", "Entertainment")
messenger = App("Messenger", "Communication")
roblox = App("Roblox", "Entertainment")


print("--- BEFORE RELATIONSHIP ---")

print("PHONE 1")
print("Model:", phone1.model)
print("Apps:", phone1.apps)

print()


print("--- BUILDING RELATIONSHIP ---")

phone1.add_app(youtube)
phone1.add_app(messenger)
phone1.add_app(roblox)


print("\n--- AFTER RELATIONSHIP ---")

print("PHONE 1")
print("Model:", phone1.model)
print("Apps:")
phone1.show_apps()