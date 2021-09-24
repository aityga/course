import psycopg2
import random as rd


conn = psycopg2.connect(
    dbname='followers', 
    user='haha', 
    password='12345', 
    host='localhost',
    port='5432'
)


logins = (
    'Atai','Sultan','Adinai','Ermek',
    'Aslan','Liazat','Salavat','Daniyar',
    'Bolot','Alymbek','Joomart','Aibek',
    'Aibek','Konstantin','Oliver','Jake',
    'Noah','James','Jack','Connor','Liam',
    'John','Harry','Callum','Mason','Robert',
    'Jacob','Jacob','Jacob','Michael','Charlie',
    'Kyle','William','William','Thomas','Joe',
    'Ethan','David','George','Reece','Michael',
    'Richard','Oscar','Rhys','Alexander','Joseph',
    'James','Charlie','James','Charles','William',
    'Damian','Daniel','Thomas','Amelia','Margaret',
    'Emma','Mary','Olivia','Samantha','Olivia',
    'Patricia','Isla','Bethany','Sophia',
    'Jennifer','Emily','Elizabeth','Isabella',
    'Elizabeth','Poppy','Joanne','Ava','Linda',
    'Ava','Megan','Mia','Barbara','Isabella','Victoria',
    'Emily','Susan','Jessica','Lauren','Abigail',
    'Margaret','Lily','Michelle','Madison','Jessica',
    'Sophie','Tracy','Charlotte','Sarah', 'qwerty',
    'test_user','test_test','user123','user_user', 'bzzzz'
)


professions = (
    'Cloud Architect',
    'Cloud Consultant',
    'Cloud Product and Project Manager',
    'Cloud Services Developer',
    'Cloud Software and Network Engineer',
    'Cloud System Administrator',
    'Cloud System Engineer',
    'Computer and Information Research Scientist',
    'Computer and Information Systems Manager',
    'Computer Network Architect',
    'Computer Systems Analyst',
    'Computer Systems Manager',
    'IT Analyst',
    'IT Coordinator',
    'Network Administrator',
    'Network Architect',
    'Network and Computer Systems Administrator',
    'Network Engineer',
    'Network Systems Administrator',
    'Senior Network Architect',
    'Senior Network Engineer',
    'Senior Network System Administrator',
    'Telecommunications Specialist',
    'Customer Support Administrator',
    'Customer Support Specialist',
    'Desktop Support Manager',
    'Desktop Support Specialist',
    'Help Desk Specialist',
    'Help Desk Technician',
    'IT Support Manager',
    'IT Support Specialist',
    'IT Systems Administrator',
    'Senior Support Specialist',
    'Senior System Administrator',
    'Support Specialist',
    'Systems Administrator',
    'Technical Specialist',
    'Technical Support Engineer',
    'Technical Support Specialist',
    'Data Center Support Specialist',
    'Data Quality Manager',
    'Database Administrator',
    'Senior Database Administrator',
    'Application Support Analyst',
    'Senior System Analyst',
    'Systems Analyst',
    'Systems Designer',
    'Chief Information Officer (CIO)',
    'Chief Technology Officer (CTO)',
    'Director of Technology',
    'IT Director',
    'IT Manager',
    'Management Information Systems Director',
    'Technical Operations Officer',
    'Information Security',
    'Security Specialist',
    'Senior Security Specialist',
    'Application Developer',
    'Applications Engineer',
    'Associate Developer',
    'Computer Programmer',
    'Developer',
    'Java Developer',
    'Junior Software Engineer',
    '.NET Developer',
    'Programmer',
    'Programmer Analyst',
    'Senior Applications Engineer',
    'Senior Programmer',
    'Senior Programmer Analyst',
    'Senior Software Engineer',
    'Senior System Architect',
    'Senior System Designer',
    'Senior Systems Software Engineer',
    'Software Architect',
    'Software Developer',
    'Software Engineer',
    'Software Quality Assurance Analyst',
    'System Architect',
    'Systems Software Engineer',
    'Front End Developer',
    'Senior Web Administrator',
    'Senior Web Developer',
    'Web Administrator',
    'Web Developer',
    'Webmaster'
)

countries = (
    'Albania',
    'Algeria',
    'Andorra',
    'Angola',
    'Antigua and Barbuda',
    'Argentina',
    'Armenia',
    'Australia',
    'Austria',
    'Azerbaijan',
    'Bahamas',
    'Bahrain',
    'Bangladesh',
    'Barbados',
    'Belarus',
    'Belgium',
    'Belize',
    'Benin',
    'Bhutan',
    'Bolivia',
    'Bosnia and Herzegovina',
    'Botswana',
    'Brazil',
    'Brunei',
    'Bulgaria',
    'Burkina Faso',
    'Burundi',
    'Cabo Verde',
    'Cambodia',
    'Cameroon',
    'Canada',
    'Central African Republic',
    'Chad',
    'Chile',
    'China',
    'Colombia',
    'Comoros',
    'Congo (Congo-Brazzaville)',
    'Costa Rica',
    'Croatia',
    'Cuba',
    'Cyprus',
    'Czechia (Czech Republic)',
    'Democratic Republic of the Congo',
    'Denmark',
    'Djibouti',
    'Dominica',
    'Dominican Republic',
    'Ecuador',
    'Egypt',
    'El Salvador',
    'Equatorial Guinea',
    'Eritrea',
    'Estonia',
    'Eswatini (fmr. "Swaziland")',
    'Ethiopia',
    'Fiji',
    'Finland',
    'France',
    'Gabon',
    'Gambia',
    'Georgia',
    'Germany',
    'Ghana',
    'Greece',
    'Grenada',
    'Guatemala',
    'Guinea',
    'Guinea-Bissau',
    'Guyana',
    'Haiti',
    'Holy See',
    'Honduras',
    'Hungary',
    'Iceland',
    'India',
    'Indonesia',
    'Iran',
    'Iraq',
    'Ireland',
    'Israel',
    'Italy',
    'Jamaica',
    'Japan',
    'Jordan',
    'Kazakhstan',
    'Kenya',
    'Kiribati',
    'Kuwait',
    'Kyrgyzstan',
    'Laos',
    'Latvia',
    'Lebanon',
    'Lesotho',
    'Liberia',
    'Libya',
    'Liechtenstein',
    'Lithuania',
    'Luxembourg',
    'Madagascar',
    'Malawi',
    'Malaysia',
    'Maldives',
    'Mali',
    'Malta',
    'Marshall Islands',
    'Mauritania',
    'Mauritius',
    'Mexico',
    'Micronesia',
    'Moldova',
    'Monaco',
    'Mongolia',
    'Montenegro',
    'Morocco',
    'Mozambique',
    'Myanmar (formerly Burma)',
    'Namibia',
    'Nauru',
    'Nepal',
    'Netherlands',
    'New Zealand',
    'Nicaragua',
    'Niger',
    'Nigeria',
    'North Korea',
    'North Macedonia',
    'Norway',
    'Oman',
    'Pakistan',
    'Palau',
    'Palestine State',
    'Panama',
    'Papua New Guinea',
    'Paraguay',
    'Peru',
    'Philippines',
    'Poland',
    'Portugal',
    'Qatar',
    'Romania',
    'Russia',
    'Rwanda',
    'Saint Kitts and Nevis',
    'Saint Lucia',
    'Saint Vincent and the Grenadines',
    'Samoa',
    'San Marino',
    'Sao Tome and Principe',
    'Saudi Arabia',
    'Senegal',
    'Serbia',
    'Seychelles',
    'Sierra Leone',
    'Singapore',
    'Slovakia',
    'Slovenia',
    'Solomon Islands',
    'Somalia',
    'South Africa',
    'South Korea',
    'South Sudan',
    'Spain',
    'Sri Lanka',
    'Sudan',
    'Suriname',
    'Sweden',
    'Switzerland',
    'Syria',
    'Tajikistan',
    'Tanzania',
    'Thailand',
    'Timor-Leste',
    'Togo',
    'Tonga',
    'Trinidad and Tobago',
    'Tunisia',
    'Turkey',
    'Turkmenistan',
    'Tuvalu',
    'Uganda',
    'Ukraine',
    'United Arab Emirates',
    'United Kingdom',
    'United States of America',
    'Uruguay',
    'Uzbekistan',
    'Vanuatu',
    'Venezuela',
    'Vietnam',
    'Yemen',
    'Zambia ',
    'Zimbabwe'
)

passwords = []
emails = []
phone_numbers = []
addresses = []
followers = tuple(rd.randint(1,10000000) for _ in range(5000))



pswd_symbols = (
    'A', 'a', 'B', 'b', 'C', 'c', 
    'D', 'd', 'E', 'e', 'F', 'f', 
    'G', 'g', 'H', 'h', 'I', 'i', 
    'J', 'j', 'K', 'k', 'L', 'l', 
    'M', 'm', 'N', 'n', 'O', 'o', 
    'P', 'p', 'Q', 'q', 'R', 'r', 
    'S', 's', 'T', 't', 'U', 'u', 
    'V', 'v', 'W', 'w', 'X', 'x', 
    'Y', 'y', 'Z', 'z', '1', '2', 
    '3', '5', '6', '7', '8', '9', '0'
)

for _ in range(5000):
    pswd = ''
    for p in range(rd.randint(8,15)):
        pswd += str(pswd_symbols[rd.randint(0, len(pswd_symbols)-1)])
    passwords.append(pswd)

domains = ('@gmail.com', '@bk.ru', '@outlook.com', '@mail.ru')
for name in logins:
    emails.append(name.lower() + str(domains[rd.randint(0,len(domains)-1)]))


codes = ('55', '70', '50', '77', '99')
for d in range(5000):
    number = '+996' + str(codes[rd.randint(0,len(codes)-1)]) + str(rd.randint(0,9)) + str(rd.randint(111111,999999))
    phone_numbers.append(number)


streets = (
    'Chui', 'Moskovskaya', 'Kievskaya', 'Toktogula', 
    'Razakova', 'Sovetskaya', 'Manasa', 'Jibek-Jolu', 
    'Erkindik', 'Pravda', 'Ahunbaeva', 'Mederova'
)
for a in range(5000):
    address = streets[rd.randint(0, len(streets)-1)] + ' ' + str(rd.randint(1,500))
    addresses.append(address)



query = '''INSERT INTO users(login, password, email, phone_number, country, address, profession, followers) VALUES '''

for _ in range(10000):
    query += f'(\
\'{logins[rd.randint(0,len(logins)-1)]}\',\
\'{passwords[rd.randint(0,len(passwords)-1)]}\',\
\'{emails[rd.randint(0,len(emails)-1)]}\',\
\'{phone_numbers[rd.randint(0,len(phone_numbers)-1)]}\',\
\'{countries[rd.randint(0,len(countries)-1)]}\',\
\'{addresses[rd.randint(0,len(addresses)-1)]}\',\
\'{professions[rd.randint(0,len(professions)-1)]}\',\
\'{followers[rd.randint(0,len(followers)-1)]}\'\
),'.replace('\\', '\\\\')

sql_query = query[:-1] + ';'


cursor = conn.cursor()

cursor.execute('CREATE TABLE users(user_id SERIAL PRIMARY KEY, login VARCHAR(20) NOT NULL, password VARCHAR(100) NOT NULL, email VARCHAR(100) NOT NULL, phone_number VARCHAR(20) NOT NULL, country VARCHAR(50) NOT NULL, address VARCHAR(50) NOT NULL, profession VARCHAR(50) NOT NULL, followers INT NOT NULL);')
cursor.execute(sql_query)
conn.commit()

cursor.execute('UPDATE users SET email = \'\' WHERE user_id % 132 = 0;')
cursor.execute('UPDATE users SET address = \'False\' WHERE user_id % 132 = 0 AND user_id % 12 = 0;')
cursor.execute('UPDATE users SET profession = \'Unemployed\' WHERE country = \'Guyana\' OR country = \'Croatia\';')
cursor.execute('UPDATE users SET phone_number = \'000000000000\' WHERE phone_number LIKE \'%995%\' OR phone_number LIKE \'%991%\';')
cursor.execute('UPDATE users SET password = \'qwerty\' WHERE address LIKE \'%kov%\' OR country LIKE \'%stan%\';')
conn.commit()

cursor.close()
conn.close()
