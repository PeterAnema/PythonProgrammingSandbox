from datetime import datetime

REFERENTIE_WAARDEN = {
    'cholesterol': {}
}


def parse_datetime_string(datetime_string = None, format_string = None):
    if datetime_string is None:
        dt = datetime.now()

    elif type(datetime_string) == datetime:
        dt = datetime_string

    else:
        if format_string is not None:
            dt = datetime.strptime(datetime_string, format_string)

        else:
            if len(datetime_string) == 10:
                dt = datetime.strptime(datetime_string, "%Y-%m-%d")
            elif len(datetime_string) == 16:
                dt = datetime.strptime(datetime_string, "%Y-%m-%d %H:%M")
            elif len(datetime_string) == 19:
                dt = datetime.strptime(datetime_string, "%Y-%m-%d %H:%M:%S")
            else:
                dt = datetime.strptime(datetime_string, "%c")

    return dt


class Patient:

    def __init__(self, id, gender, date_of_birth):
        self.id = id
        self.gender = gender
        self.date_of_birth = parse_datetime_string(date_of_birth, '%Y-%m-%d')

    @property
    def age(self):
        return (datetime.now() - self.date_of_birth).days // 365.2425

    def __str__(self):
        return '%s %s %d' % (self.id, self.gender[0].upper(), self.age)


class Bepaling:

    def __init__(self, bepaling, patient, afname_moment, waarde):
        self.bepaling = bepaling
        self.patient = patient
        self.afname_moment = parse_datetime_string(afname_moment)
        self.waarde = waarde
        self.normal_low = None
        self.normal_high = None

    def set_normaal_values(self, normal_low = None, normal_high = None):
        self.normal_low = normal_low
        self.normal_high = normal_high

    def is_normaal(self):
        return (not self.is_to_low()) and (not self.is_to_high())

    def is_to_low(self):
        return (self.normal_low is not None and self.waarde < self.normal_low)

    def is_to_high(self):
        return (self.normal_high is not None and self.waarde > self.normal_high)

    def str_normal(self):
        if self.is_normaal():
            return 'OK'
        elif self.is_to_high():
            return '+'
        else:
            return '-'

    def rank(self, asc1=True, asc2=True):
        m = self.afname_moment if asc1 else datetime.now() - self.afname_moment
        b = self.bepaling if asc2 else ''.join(chr(ord('z')-ord(c)+ord('a')) for c in self.bepaling)
        return m, b

    def __eq__(self, other):
        return self.rank() == other.rank()
    def __ne__(self, other):
        return self.rank() != other.rank()
    def __lt__(self, other):
        return self.rank() < other.rank()
    def __le__(self, other):
        return self.rank() <= other.rank()
    def __gt__(self, other):
        return self.rank() > other.rank()
    def __ge__(self, other):
        return self.rank() >= other.rank()

    def __str__(self):
        return "%s - %-20s %20s %16.3f %s" % (self.patient,
                                              self.bepaling,
                                              self.afname_moment.strftime("%Y-%m-%d %H:%M"),
                                              self.waarde,
                                              self.str_normal())



class Cholesterol(Bepaling):

    BEPALING = 'Cholesterol'
    NORMAL_LOW = 10
    NORMAL_HIGH = 35

    def __init__(self, patient, waarde, afname_moment):
        super().__init__(Cholesterol.BEPALING, patient, waarde, afname_moment)
        self.set_normaal_values(Cholesterol.NORMAL_LOW, Cholesterol.NORMAL_HIGH)

class HB(Bepaling):

    BEPALING = 'HB'
    NORMAL_LOW = 10
    NORMAL_HIGH = 35

    def __init__(self, patient, waarde, afname_moment):
        super().__init__(HB.BEPALING, patient, waarde, afname_moment)
        self.set_normaal_values(HB.NORMAL_LOW, HB.NORMAL_HIGH)


# ==================================== client code

patient = Patient('Anema', 'man', '1956-08-20')

bepalingen = []

bepalingen.append( HB(          patient, "2018-11-07 12:00", 1.0) )
bepalingen.append( Cholesterol( patient, "2018-11-06 12:00", 200.0) )
bepalingen.append( Cholesterol( patient, "2018-11-07 12:00", 20.0) )
bepalingen.append( HB(          patient, "2018-11-04",       1.0) )
bepalingen.append( HB(          patient, "2018-11-06 12:00", 20.0) )

for bepaling in sorted(bepalingen):
    print(bepaling)