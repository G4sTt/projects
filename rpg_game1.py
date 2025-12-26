class Character:
    def __init__(self, name, sex, age, level = 1):
        self.name = name
        self.sex = sex
        self.age = age
        self.level = level # базовые настройки для всех

    def get_name(self):
        return f"Имя персонажа - {self.name}"

    def run(self):
        return f"{self.name} бежит"

    def jump(self):
        return f"{self.name} прыгает"


class Human(Character):
    def __init__(self, name, sex, age, level = 1,
                 health = 100,
                 stamina = 100,
                 ultimate = "Берсерк",
                 hill_hp = 0,
                 attack_power = 5,
                 super_attack = 30):
        super().__init__(name, sex, age, level)
        self.max_health = health
        self.health = health
        self.stamina = stamina
        self.ultimate = ultimate
        self.attack_power = attack_power
        self.hill_hp = hill_hp
        self.super_attack = super_attack

    def show_level(self):
        return f"Текущий уровень: {self.level}"

    def show_health(self):
        return f"Здоровье {self.name}: {self.health}/{self.max_health}"

    def show_stamina(self):
        return f"Выносливость {self.name}: {self.stamina}"

    def use_ultimate(self):
        return f"Ультимэйт '{self.ultimate}' активирован!"

    def attack(self, target):
        """Атаковать другого персонажа"""
        if self.health <= 0:
            return f"{self.name} не может атаковать, так как мёртв"

        if target.health <= 0:
            return f"{target.name} уже мёртв"
        target.health -= self.attack_power

        if target.health <= 0:
            target.health = 0
            return (f"{self.name} атакует {target.name} и наносит {self.attack_power} урона!\n"
                    f"{target.name} повержен!")

        return (f"{self.name} атакует {target.name} и наносит {self.attack_power} урона!\n"
                f"Здоровье {target.name}: {target.health}/{target.max_health}")

    def take_damage(self, damage_amount):
        """Получить урон"""
        self.health -= damage_amount
        if self.health <= 0:
            self.health = 0
            return f"{self.name} получает {damage_amount} урона и умирает!"
        return f"{self.name} получает {damage_amount} урона. Здоровье: {self.health}/{self.max_health}"


class Angel(Human): #  от Human наследуется, так легче
    def __init__(self, name, sex, age):
        super().__init__(name, sex, age, level = 1,
                         health = 130,
                         stamina = 80,
                         ultimate = "Божественное благословение",
                         attack_power = 3,
                         hill_hp = 30)

    def fly(self):    # полет - как уклонение
        if self.stamina >= 20:
            self.stamina -= 20
            return f"{self.name} парит в воздухе с сияющим нимбом (стамина: {self.stamina})"
        return f"{self.name} слишком устал для полёта"

    def heal(self, target=None):
        """Лечить себя или другого персонажа"""
        if target is None:
            target = self

        if not hasattr(target, 'max_health'):
            target.max_health = target.health  # Если нет max_health, создаем

        if target.health >= target.max_health:
            return f"У {target.name} здоровье уже максимальное ({target.health}/{target.max_health})"
        target.health += self.hill_hp

        if target.health > target.max_health:
            target.health = target.max_health

        return (f"{self.name} исцеляет {target.name} на {self.hill_hp} HP.\n"
                f"Здоровье {target.name}: {target.health}/{target.max_health}")


class Orc(Human):
    def __init__(self, name, sex, age):
        super().__init__(name, sex, age, level = 1,
                         health = 180,
                         stamina = 50,
                         ultimate = "Раскаты грома",
                         attack_power = 15,
                         hill_hp = 0)

    def use_ultimate(self, target):
        """Специальная атака орка - Раскаты грома"""
        if self.stamina >= 50:
            self.stamina -= 50
            ult_power = 50
            target.health -= ult_power

            if target.health <= 0:
                target.health = 0
                return (f"{self.name} использует '{self.ultimate}' на {target.name}!\n"
                        f"Нанесено {ult_power} урона! {target.name} повержен!")

            return (f"{self.name} использует '{self.ultimate}' на {target.name}!\n"
                    f"Нанесено {ult_power} урона! Здоровье {target.name}: {target.health}/{target.max_health}")

        return f"{self.name} слишком устал для использования ультимэйта! (Нужно 50 стамины, есть {self.stamina})"


# test
if __name__ == "__main__":
    name1 = input("Имя человека: ")
    name2 = input("Имя ангела: ")
    name3 = input("Имя орка: ")

    human = Human(name1, "мужской", 25)
    angel = Angel(name2, "мужской", 1000)
    orc = Orc(name3, "мужской", 35)

    print("\n=== Начало битвы ===")
    print(f"{human.show_health()}")
    print(f"{angel.show_health()}")
    print(f"{orc.show_health()}")

    print("\n=== Атаки ===")
    print(human.attack(angel))
    print(angel.attack(orc))
    print(orc.attack(human))

    print("\n=== Специальные способности ===")
    print(angel.fly())
    print(angel.heal())  # Ангел лечит себя
    print(orc.use_ultimate(angel))  # Орк использует ультимэйт на ангела

    print("\n=== Итоговое состояние ===")
    print(f"{human.show_health()}")
    print(f"{angel.show_health()}")
    print(f"{orc.show_health()}")