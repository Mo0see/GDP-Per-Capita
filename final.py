# Christopher Soscia | ECO-101 Final Project

# This is my final project, This is an algorithm that will (somewhat) predict the future GDP per capita of the united states.
# The initial data is based of numbers from google's data charts [ https://www.google.com/publicdata/explore?ds=d5bncppjof8f9_&met_y=ny_gdp_pcap_cd&idim=country:USA:GBR:CAN&hl=en&dl=en ]
# The latest data was from 2017, therefore thats why it starts from 2017

# This is where i declared the base data for the calculations
firstYear = 1960
secondYear = 2017

firstGDP = 3007.12
secondGDP = 59531.66

targetYear = int(input('Pick a year in the future: '))

# This function calculated the Rate of Change using the change in Y over thechange in X, very basic math but very effective
def calculate ():
    gdpDiff = (secondGDP - firstGDP)
    yearDiff = (secondYear - firstYear)

    return (gdpDiff / yearDiff)

# After the Rate of Change is calculated this function will do a quick calculation using the year specified and it
# will loop until it hits your desired year, while printing the data for each individual year
def predict ():
    roc = calculate()

    currentYear = secondYear
    currentGDP = secondGDP

    for i in range((targetYear - secondYear) + 1):
        currentYear = secondYear + i
        currentGDP += roc
    
        print('Year: {}\nGDP: ${}\n'.format(currentYear, currentGDP))

predict()
