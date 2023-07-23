useradmin = {
    'anbi': {
        'name': 'Anupam Biswas',
        'doj': '20-07-2023',
        'department': 'Compositing',
        'designation': 'Compositing-lead',
        'email': 'ripanbiswas007@gmail.com',
        'username': 'anupam-b',
        'on-leave': True
    },
    'subi': {
        'name': 'Sumi Biswas(Basu)',
        'doj': '2-01-2023',
        'department': 'production',
        'designation': 'Production maneger',
        'email': 'bindiya1900@gmail.com',
        'username': 'sumi-b',
        'on-leave': False
    },
    'acbi': {
        'name': 'Achinto Biswas',
        'doj': '19-01-2023',
        'department': 'Compositing',
        'designation': 'Artist',
        'email': 'achintobiswas25@gmail.com',
        'username': 'achinto-b',
        'on-leave': False
    },
    'gobi': {
        'name': 'Gauri Biswas',
        'doj': '1-05-2022',
        'department': 'Hr',
        'designation': 'head HR',
        'email': 'gouribiswas065@gmail.com',
        'username': 'gauri-b',
        'on-leave': False
    },
    'aybi': {
        'name': 'Ayush Biswas',
        'doj': '7-03-2023',
        'department': 'Roto',
        'designation': 'Artist',
        'email': 'ayushbiswas16@gmail.com',
        'username': 'ayush-b',
        'on-leave': True
    },
    'ankbi': {
        'name': 'Ankush Biswas',
        'doj': '27-07-2022',
        'department': 'Roto',
        'designation': 'Artist',
        'email': 'ankushbiswas23@gmail.com',
        'username': 'ankush-b',
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
