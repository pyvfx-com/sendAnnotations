useradmin = {
    'anbi': {
        'name': 'Anupam Biswas',
        'on-leave': True
    },
    'subi': {
        'name': 'Sumi Biswas(Basu)',
        'on-leave': False
    },
    'acbi': {
        'name': 'Achinto Biswas',
        'on-leave': False
    },
    'gobi': {
        'name': 'Gauri Biswas',
        'on-leave': False
    },
    'aybi': {
        'name': 'Ayush Biswas',
        'on-leave': True
    },
    'ankbi': {
        'name': 'Ankush Biswas',
        'on-leave': True
    }
}


class htmldigger_database:
    @staticmethod
    def name_list():
        names = list(useradmin[name]['name'] for name in useradmin)
        return names

    def get_data_by_name(name):
        for user in useradmin.values():
            if user['name'] == name:
                return user
        return None


if __name__ == '__main__':
    input_name = input("Please enter a name: ")
    user_data = htmldigger_database.get_data_by_name(input_name)
    print("*" * 50)
    if user_data:
        print("User found:")
        print("Name:", user_data['name'])
        print("Email is here :", user_data['email'])
    else:
        print("User not found.")

    print("*" * 50)
