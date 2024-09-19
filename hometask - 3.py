# hometask - 3


class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        result = self.__cpu + self.__memory
        print(f'Результат вычисления: {self.__cpu} + {self.__memory} = {result}')
        return result

    def __str__(self):
        return f'Компьютер (CPU: {self.__cpu}, Память: {self.__memory} ГБ)'

    def __lt__(self, other):
        return self.__memory < other.__memory

    def __gt__(self, other):
        return self.__memory > other.__memory

    def __eq__(self, other):
        return self.__memory == other.__memory

    def __ne__(self, other):
        return self.__memory != other.__memory

    def __le__(self, other):
        return self.__memory <= other.__memory

    def __ge__(self, other):
        return self.__memory >= other.__memory


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        try:
            sim_card = self.__sim_cards_list[sim_card_number - 1]
            print(f"Звонок на номер {call_to_number} с SIM-{sim_card_number}: {sim_card}")
        except IndexError:
            print(f"SIM-карта {sim_card_number} не существует!")

    def __str__(self):
        return f'Телефон (SIM-карты: {", ".join(self.__sim_cards_list)})'


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        print(f"Маршрут до {location}...")

    def __str__(self):
        return f'Смартфон (CPU: {self.cpu}, Память: {self.memory} ГБ, SIM-карты: {", ".join(self.sim_cards_list)})'


computer = Computer(4, 16)
phone = Phone(["Beeline", "Megacom"])
smartphone1 = SmartPhone(8, 64, ["O!", "Megacom"])
smartphone2 = SmartPhone(6, 128, ["Beeline", "O!"])

print(computer)
print(phone)
print(smartphone1)
print(smartphone2)

computer.make_computations()

phone.call(1, "+996 777 99 88 11")
phone.call(2, "+996 555 77 66 55")
phone.call(3, "+996 222 33 44 22")  

smartphone1.use_gps("Центральный Парк")
smartphone1.call(1, "+996 707 88 77 66")
smartphone1.make_computations()

if computer < smartphone1:
    print("Компьютер имеет меньше памяти, чем Смартфон1.")
else:
    print("Компьютер не имеет меньше памяти, чем Смартфон1.")

if smartphone1 > smartphone2:
    print("Смартфон1 имеет больше памяти, чем Смартфон2.")
else:
    print("Смартфон1 не имеет больше памяти, чем Смартфон2.")

if smartphone1 == smartphone2:
    print("Смартфон1 и Смартфон2 имеют одинаковую память.")
else:
    print("Смартфон1 и Смартфон2 не имеют одинаковую память.")

total_memory = computer.memory + smartphone1.memory
print(f"Сумма памяти компьютера и Смартфона1: {total_memory} ГБ")

