import sys


def Time(tm):
    try:
        if type(tm)==str:
            t = ''.join([i for i in tm if not i.isalpha()])
            if ':' not in t:
                if t.isspace() or t == '':
                    return None
                else:
                    return float(t)
            else:
                t = t.split(':')
                out = 0
                out += float(t[0])*60
                out += float(t[1])
            return out
        else:
            return str(int(tm//60))+':'+str(tm%60)
    except Exception as e:
        print(e)
        print(t)
        sys.exit(1)


def ismark(mark):
    m = ''.join([i.lower() for i in mark])
    return not (m[:2] == 'dn' or m == 'nt' or m == 'dq' or m == 'fs')

 
def event_classification():
    dic = {
        'Field' :
            [
                'SP',
                'LJ',
                'HJ',
                'PV',
                'WT',
                'TJ',
                'DT',
                'JT',
                'HT',
                'Hep',
                'Dec',
                'Pent'
            ],
        'Track' :
            [
                '8K',
                '5000',
                '800',
                '1500',
                '4x400',
                '3000',
                'Mile',
                '10K',
                '200',
                '400',
                'DMR',
                '60',
                '3000S',
                '10000',
                '60H',
                '4x100',
                '4x800',
                '1000',
                '100',
                '5K',
                '110H',
                '6K',
                '400H',
                '600',
                '4.97M',
                '5M',
                '4M',
                '7K',
                '6.2M',
                '600 yd',
                '4K',
                '4x200',
                '300',
                '500',
                '6.4K',
                '55',
                '1600SMR',
                '3.1M',
                '4x1600',
                '55H',
                '4x1500',
                '6.21M',
                '4.98M',
                '4.94M',
                '6.437K',
                '6.2K',
                '6.3K',
                '4x440 yd',
                '2Mile',
                'DMR (Yd)',
                '8000K',
                '2000S',
                '5.15K',
                '4.81K',
                '4.96M',
                '7.25K',
                '7.6K',
                '4.2M',
                '4x880 yd',
                '3.8M',
                '6.44K',
                '7.5K',
                '4.8M',
                '4.1M',
                '5.9K',
                '3M',
                '4xMile',
                '3.72M',
                '1M',
                '4.2K',
                '4x1',
                '4.5M',
                '4.195M',
                '8.085K',
                '300H',
                '3.88M',
                '4x320',
                '200H',
                '6.6K',
                '4.5K',
                '3200',
                '8.4K',
                '4x300',
                '7.9K',
                '3K',
                '4.97K',
                '5.25K',
                '1600',
                '8.1K',
                '7.4K',
                '4.3M',
                '1500S',
                '3200DMR',
                '2M',
                '5000 RW',
                '8M',
                '4.96K',
                '4x220 yd',
                '7.1K',
                '7.2K',
                '150',
                '6.956K',
                '2000',
                '7.71K',
                '3.92K',
                '8.2K',
                '5000m',
                '4.7M',
                '4.8K',
                '8.042K',
                '3.11M',
                '8.369K',
                '1200',
                '4.25M',
                '1100',
                '6.387K',
                '8.067K',
                '5.2M',
                '5.1M',
                '110SH',
                '3.12M',
                '4.87M',
                '3.73M'
            ]
    }
    return dic


def string_to_distance(event):
    try:
        if event[-1].upper() == 'K':
            return float(''.join([e for e in event if e.isnumeric() or e == '.'])) * 1000
        elif event[-1].upper() == 'M':
            return float(''.join([e for e in event if e.isnumeric() or e == '.'])) * 1609.34
        elif event[1].upper() == 'X':
            # relays are -
            m_per_unit = 1
            if ''.join([e.lower() for e in event[-2:]]) == 'yd':
                m_per_unit = 0.9144
            elif ''.join([e.lower() for e in event[-4:]]) == 'mile':
                return -1609.34 * 4
            return -float(''.join([e for e in event[1:] if e.isnumeric() or e == '.'])) * m_per_unit * 4
        elif ''.join([e.lower() for e in event[:3]]) == 'dmr':
            return -4000.0
        elif ''.join([e.lower() for e in event[-2:]]) == 'yd':
            return float(''.join([e for e in event if e.isnumeric() or e == '.'])) * 0.9144
        elif ''.join([e.lower() for e in event]) == 'mile':
            return 1609.34
        elif 'mr' in ''.join([e.lower() for e in event]):
            return -float(''.join([e for e in event if e.isnumeric() or e == '.']))
        else:
            return float(''.join([e for e in event if e.isnumeric() or e == '.']))
    except Exception as e:
        print(e)
        print(event)
        sys.exit(1)


def get_records():
    records = {
        'Outdoor' : {
            '100' : '9.96',
            '200' : '20.15',
            '400' : '44.09',
            '800' : '1:44.44',
            '1500' : '3:37.35',
            '3000S' : '8:14.17',
            '5000' : '13:22.64',
            '10000' : '27:48.06',
            '110H' : '13.0h',
            '400H' : '47.58'
        },
        'Indoor' : {
            '60': '6.54',
            '200': '20.67',
            '400': '45.67',
            '800': '1:46.27',
            'Mile': '3:56.74',
            '3000': '7:50.81',
            '5000': '13:41.08',
            '60H': '7.53h',
        }
    }
    return records
