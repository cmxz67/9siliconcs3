class Device:

    def __init__(self, model, storage, limit):
        self.model = model
        self.storage = storage
        self.__limit = limit

    def show_storage(self):
        print("Storage:", self.storage, "GB")

    def get_limit(self):
        return self.__limit

class App:

    def __init__(self, name, category):
        self.name = name
        self.category = category

class Battery:

    def __init__(self, capacity):
        self.capacity = capacity

    def show_battery(self):
        print("Battery:", self.capacity, "mAh")

class Cellphone(Device):

    def __init__(self, model, apps, storage, limit, battery_capacity):
        super().__init__(model, storage, limit)

        self.apps = apps
        self.battery = Battery(battery_capacity)

    def add_app(self, app):
        self.apps.append(app)
        print(app.name, "was added to", self.model)

    def show_apps(self):
        for app in self.apps:
            print("App:", app.name)
            print("Category:", app.category)


phone1 = Cellphone(
    "Samsung A15",
    [],
    64,
    128,
    5000
)

phone2 = Cellphone(
    "Samsung A06",
    [],
    32,
    64,
    4000
)

youtube = App("YouTube", "Entertainment")
messenger = App("Messenger", "Communication")
roblox = App("Roblox", "Entertainment")


print("INHERITANCE:")
print("Cellphone using Device's show_storage() and get_limit():")
print("PHONE 1")
print("Model:", phone1.model)
phone1.show_storage()
print("Limit:", phone1.get_limit(), "GB")

print()

print("COMPOSITION:")
print("PHONE 1's own Battery object:")
phone1.battery.show_battery()
print("(phone1 made this Battery itself in its __init__ -")
print(" if phone1 is deleted, phone1.battery is deleted with it.)")

print()

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
phone1.battery.show_battery()

