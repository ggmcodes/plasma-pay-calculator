#!/usr/bin/env python3
"""Generate Round 3: 47 State-Level Plasma Center Guide Pages"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_batch1_centers import make_en_page, make_faq, AFFILIATE_BLOCK, PRO_TOOLKIT, related_reading, footer_related

BLOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'blog')

# ============================================================
# State data: name, slug suffix, abbreviation, major metros,
# region description, approximate center count, population,
# chains present, top cities for plasma centers
# ============================================================

STATES = [
    {
        "name": "Alabama",
        "slug": "alabama",
        "abbr": "AL",
        "population": "5.1 million",
        "region": "the Deep South",
        "center_count": "20+",
        "chains": ["CSL Plasma", "BioLife", "Octapharma", "Grifols"],
        "metros": ["Birmingham", "Huntsville", "Montgomery", "Mobile", "Tuscaloosa"],
        "top_cities": [
            ("Birmingham", None),
            ("Huntsville", None),
            ("Montgomery", None),
            ("Mobile", None),
            ("Tuscaloosa", None),
        ],
    },
    {
        "name": "Alaska",
        "slug": "alaska",
        "abbr": "AK",
        "population": "733,000",
        "region": "the Pacific Northwest",
        "center_count": "2-3",
        "chains": ["CSL Plasma"],
        "metros": ["Anchorage", "Fairbanks", "Juneau"],
        "top_cities": [
            ("Anchorage", None),
            ("Fairbanks", None),
        ],
    },
    {
        "name": "Arizona",
        "slug": "arizona",
        "abbr": "AZ",
        "population": "7.4 million",
        "region": "the Southwest",
        "center_count": "35+",
        "chains": ["CSL Plasma", "BioLife", "Octapharma", "Grifols"],
        "metros": ["Phoenix", "Tucson", "Mesa", "Scottsdale", "Chandler", "Tempe"],
        "top_cities": [
            ("Phoenix", "/blog/best-plasma-center-phoenix-arizona.html"),
            ("Tucson", None),
            ("Mesa", None),
            ("Scottsdale", None),
            ("Chandler", None),
            ("Tempe", None),
        ],
    },
    {
        "name": "Arkansas",
        "slug": "arkansas",
        "abbr": "AR",
        "population": "3.0 million",
        "region": "the South Central US",
        "center_count": "12+",
        "chains": ["CSL Plasma", "BioLife", "Octapharma", "Grifols"],
        "metros": ["Little Rock", "Fort Smith", "Fayetteville", "Springdale", "Jonesboro"],
        "top_cities": [
            ("Little Rock", None),
            ("Fort Smith", None),
            ("Fayetteville", None),
            ("Springdale", None),
            ("Jonesboro", None),
        ],
    },
    {
        "name": "Colorado",
        "slug": "colorado",
        "abbr": "CO",
        "population": "5.9 million",
        "region": "the Mountain West",
        "center_count": "25+",
        "chains": ["CSL Plasma", "BioLife", "Octapharma", "Grifols"],
        "metros": ["Denver", "Colorado Springs", "Aurora", "Fort Collins", "Lakewood", "Boulder"],
        "top_cities": [
            ("Denver", "/blog/best-plasma-center-denver-colorado.html"),
            ("Colorado Springs", None),
            ("Aurora", None),
            ("Fort Collins", None),
            ("Lakewood", None),
        ],
    },
    {
        "name": "Connecticut",
        "slug": "connecticut",
        "abbr": "CT",
        "population": "3.6 million",
        "region": "New England",
        "center_count": "8+",
        "chains": ["CSL Plasma", "BioLife", "Octapharma", "Grifols"],
        "metros": ["Bridgeport", "New Haven", "Hartford", "Stamford", "Waterbury"],
        "top_cities": [
            ("Bridgeport", None),
            ("New Haven", None),
            ("Hartford", None),
            ("Stamford", None),
            ("Waterbury", None),
        ],
    },
    {
        "name": "Delaware",
        "slug": "delaware",
        "abbr": "DE",
        "population": "1.0 million",
        "region": "the Mid-Atlantic",
        "center_count": "4+",
        "chains": ["CSL Plasma", "BioLife", "Grifols"],
        "metros": ["Wilmington", "Dover", "Newark"],
        "top_cities": [
            ("Wilmington", None),
            ("Dover", None),
            ("Newark", None),
        ],
    },
    {
        "name": "Washington DC",
        "slug": "washington-dc",
        "abbr": "DC",
        "population": "689,000",
        "region": "the Mid-Atlantic",
        "center_count": "5+",
        "chains": ["CSL Plasma", "BioLife", "Octapharma", "Grifols"],
        "metros": ["Washington DC", "Capitol Hill", "Georgetown", "Dupont Circle"],
        "top_cities": [
            ("Washington DC", None),
            ("Arlington (VA)", None),
            ("Bethesda (MD)", None),
        ],
    },
    {
        "name": "Georgia",
        "slug": "georgia",
        "abbr": "GA",
        "population": "10.9 million",
        "region": "the Southeast",
        "center_count": "35+",
        "chains": ["CSL Plasma", "BioLife", "Octapharma", "Grifols"],
        "metros": ["Atlanta", "Augusta", "Columbus", "Savannah", "Macon", "Athens"],
        "top_cities": [
            ("Atlanta", "/blog/best-plasma-center-atlanta-georgia.html"),
            ("Augusta", None),
            ("Columbus", None),
            ("Savannah", None),
            ("Macon", None),
            ("Athens", None),
        ],
    },
    {
        "name": "Hawaii",
        "slug": "hawaii",
        "abbr": "HI",
        "population": "1.4 million",
        "region": "the Pacific Islands",
        "center_count": "2-3",
        "chains": ["CSL Plasma"],
        "metros": ["Honolulu", "Pearl City", "Hilo"],
        "top_cities": [
            ("Honolulu", None),
            ("Pearl City", None),
        ],
    },
    {
        "name": "Idaho",
        "slug": "idaho",
        "abbr": "ID",
        "population": "1.9 million",
        "region": "the Pacific Northwest",
        "center_count": "8+",
        "chains": ["CSL Plasma", "BioLife", "Grifols"],
        "metros": ["Boise", "Meridian", "Nampa", "Idaho Falls", "Pocatello"],
        "top_cities": [
            ("Boise", None),
            ("Meridian", None),
            ("Nampa", None),
            ("Idaho Falls", None),
            ("Pocatello", None),
        ],
    },
    {
        "name": "Illinois",
        "slug": "illinois",
        "abbr": "IL",
        "population": "12.6 million",
        "region": "the Midwest",
        "center_count": "40+",
        "chains": ["CSL Plasma", "BioLife", "Octapharma", "Grifols"],
        "metros": ["Chicago", "Aurora", "Rockford", "Joliet", "Naperville", "Springfield", "Peoria"],
        "top_cities": [
            ("Chicago", "/blog/best-plasma-center-chicago-illinois.html"),
            ("Aurora", None),
            ("Rockford", None),
            ("Springfield", None),
            ("Peoria", None),
            ("Joliet", None),
        ],
    },
    {
        "name": "Indiana",
        "slug": "indiana",
        "abbr": "IN",
        "population": "6.8 million",
        "region": "the Midwest",
        "center_count": "30+",
        "chains": ["CSL Plasma", "BioLife", "Octapharma", "Grifols"],
        "metros": ["Indianapolis", "Fort Wayne", "Evansville", "South Bend", "Carmel", "Bloomington"],
        "top_cities": [
            ("Indianapolis", None),
            ("Fort Wayne", None),
            ("Evansville", None),
            ("South Bend", None),
            ("Bloomington", None),
        ],
    },
    {
        "name": "Iowa",
        "slug": "iowa",
        "abbr": "IA",
        "population": "3.2 million",
        "region": "the Midwest",
        "center_count": "15+",
        "chains": ["CSL Plasma", "BioLife", "Octapharma", "Grifols"],
        "metros": ["Des Moines", "Cedar Rapids", "Davenport", "Sioux City", "Iowa City"],
        "top_cities": [
            ("Des Moines", None),
            ("Cedar Rapids", None),
            ("Davenport", None),
            ("Sioux City", None),
            ("Iowa City", None),
        ],
    },
    {
        "name": "Kansas",
        "slug": "kansas",
        "abbr": "KS",
        "population": "2.9 million",
        "region": "the Great Plains",
        "center_count": "12+",
        "chains": ["CSL Plasma", "BioLife", "Octapharma", "Grifols"],
        "metros": ["Wichita", "Overland Park", "Kansas City", "Olathe", "Topeka"],
        "top_cities": [
            ("Wichita", None),
            ("Overland Park", None),
            ("Kansas City", None),
            ("Topeka", None),
            ("Lawrence", None),
        ],
    },
    {
        "name": "Kentucky",
        "slug": "kentucky",
        "abbr": "KY",
        "population": "4.5 million",
        "region": "the Southeast",
        "center_count": "18+",
        "chains": ["CSL Plasma", "BioLife", "Octapharma", "Grifols"],
        "metros": ["Louisville", "Lexington", "Bowling Green", "Owensboro", "Covington"],
        "top_cities": [
            ("Louisville", None),
            ("Lexington", None),
            ("Bowling Green", None),
            ("Owensboro", None),
            ("Covington", None),
        ],
    },
    {
        "name": "Louisiana",
        "slug": "louisiana",
        "abbr": "LA",
        "population": "4.6 million",
        "region": "the Gulf Coast",
        "center_count": "18+",
        "chains": ["CSL Plasma", "BioLife", "Octapharma", "Grifols"],
        "metros": ["New Orleans", "Baton Rouge", "Shreveport", "Lafayette", "Lake Charles"],
        "top_cities": [
            ("New Orleans", None),
            ("Baton Rouge", None),
            ("Shreveport", None),
            ("Lafayette", None),
            ("Lake Charles", None),
        ],
    },
    {
        "name": "Maine",
        "slug": "maine",
        "abbr": "ME",
        "population": "1.4 million",
        "region": "New England",
        "center_count": "3-5",
        "chains": ["CSL Plasma", "BioLife"],
        "metros": ["Portland", "Lewiston", "Bangor"],
        "top_cities": [
            ("Portland", None),
            ("Lewiston", None),
            ("Bangor", None),
        ],
    },
    {
        "name": "Maryland",
        "slug": "maryland",
        "abbr": "MD",
        "population": "6.2 million",
        "region": "the Mid-Atlantic",
        "center_count": "15+",
        "chains": ["CSL Plasma", "BioLife", "Octapharma", "Grifols"],
        "metros": ["Baltimore", "Columbia", "Germantown", "Silver Spring", "Waldorf", "Frederick"],
        "top_cities": [
            ("Baltimore", None),
            ("Columbia", None),
            ("Silver Spring", None),
            ("Frederick", None),
            ("Waldorf", None),
        ],
    },
    {
        "name": "Massachusetts",
        "slug": "massachusetts",
        "abbr": "MA",
        "population": "7.0 million",
        "region": "New England",
        "center_count": "12+",
        "chains": ["CSL Plasma", "BioLife", "Octapharma", "Grifols"],
        "metros": ["Boston", "Worcester", "Springfield", "Lowell", "Cambridge", "New Bedford"],
        "top_cities": [
            ("Boston", None),
            ("Worcester", None),
            ("Springfield", None),
            ("Lowell", None),
            ("New Bedford", None),
        ],
    },
    {
        "name": "Michigan",
        "slug": "michigan",
        "abbr": "MI",
        "population": "10.0 million",
        "region": "the Great Lakes",
        "center_count": "35+",
        "chains": ["CSL Plasma", "BioLife", "Octapharma", "Grifols"],
        "metros": ["Detroit", "Grand Rapids", "Warren", "Sterling Heights", "Ann Arbor", "Lansing", "Flint"],
        "top_cities": [
            ("Detroit", None),
            ("Grand Rapids", None),
            ("Ann Arbor", None),
            ("Lansing", None),
            ("Flint", None),
            ("Warren", None),
        ],
    },
    {
        "name": "Minnesota",
        "slug": "minnesota",
        "abbr": "MN",
        "population": "5.7 million",
        "region": "the Upper Midwest",
        "center_count": "18+",
        "chains": ["CSL Plasma", "BioLife", "Octapharma", "Grifols"],
        "metros": ["Minneapolis", "Saint Paul", "Rochester", "Duluth", "Bloomington", "Brooklyn Park"],
        "top_cities": [
            ("Minneapolis", None),
            ("Saint Paul", None),
            ("Rochester", None),
            ("Duluth", None),
            ("Bloomington", None),
        ],
    },
    {
        "name": "Mississippi",
        "slug": "mississippi",
        "abbr": "MS",
        "population": "2.9 million",
        "region": "the Deep South",
        "center_count": "12+",
        "chains": ["CSL Plasma", "BioLife", "Octapharma", "Grifols"],
        "metros": ["Jackson", "Gulfport", "Southaven", "Hattiesburg", "Biloxi"],
        "top_cities": [
            ("Jackson", None),
            ("Gulfport", None),
            ("Hattiesburg", None),
            ("Biloxi", None),
            ("Southaven", None),
        ],
    },
    {
        "name": "Missouri",
        "slug": "missouri",
        "abbr": "MO",
        "population": "6.2 million",
        "region": "the Midwest",
        "center_count": "25+",
        "chains": ["CSL Plasma", "BioLife", "Octapharma", "Grifols"],
        "metros": ["Kansas City", "St. Louis", "Springfield", "Columbia", "Independence", "Lee's Summit"],
        "top_cities": [
            ("Kansas City", None),
            ("St. Louis", None),
            ("Springfield", None),
            ("Columbia", None),
            ("Independence", None),
        ],
    },
    {
        "name": "Montana",
        "slug": "montana",
        "abbr": "MT",
        "population": "1.1 million",
        "region": "the Northern Rockies",
        "center_count": "3-5",
        "chains": ["CSL Plasma", "BioLife"],
        "metros": ["Billings", "Missoula", "Great Falls", "Bozeman"],
        "top_cities": [
            ("Billings", None),
            ("Missoula", None),
            ("Great Falls", None),
        ],
    },
    {
        "name": "Nebraska",
        "slug": "nebraska",
        "abbr": "NE",
        "population": "2.0 million",
        "region": "the Great Plains",
        "center_count": "10+",
        "chains": ["CSL Plasma", "BioLife", "Octapharma", "Grifols"],
        "metros": ["Omaha", "Lincoln", "Bellevue", "Grand Island"],
        "top_cities": [
            ("Omaha", None),
            ("Lincoln", None),
            ("Bellevue", None),
            ("Grand Island", None),
        ],
    },
    {
        "name": "Nevada",
        "slug": "nevada",
        "abbr": "NV",
        "population": "3.2 million",
        "region": "the Southwest",
        "center_count": "15+",
        "chains": ["CSL Plasma", "BioLife", "Octapharma", "Grifols"],
        "metros": ["Las Vegas", "Henderson", "Reno", "North Las Vegas", "Sparks"],
        "top_cities": [
            ("Las Vegas", "/blog/best-plasma-center-las-vegas-nevada.html"),
            ("Henderson", None),
            ("Reno", None),
            ("North Las Vegas", None),
            ("Sparks", None),
        ],
    },
    {
        "name": "New Hampshire",
        "slug": "new-hampshire",
        "abbr": "NH",
        "population": "1.4 million",
        "region": "New England",
        "center_count": "3-5",
        "chains": ["CSL Plasma", "BioLife"],
        "metros": ["Manchester", "Nashua", "Concord"],
        "top_cities": [
            ("Manchester", None),
            ("Nashua", None),
            ("Concord", None),
        ],
    },
    {
        "name": "New Jersey",
        "slug": "new-jersey",
        "abbr": "NJ",
        "population": "9.3 million",
        "region": "the Mid-Atlantic",
        "center_count": "20+",
        "chains": ["CSL Plasma", "BioLife", "Octapharma", "Grifols"],
        "metros": ["Newark", "Jersey City", "Paterson", "Elizabeth", "Edison", "Trenton"],
        "top_cities": [
            ("Newark", None),
            ("Jersey City", None),
            ("Paterson", None),
            ("Elizabeth", None),
            ("Trenton", None),
        ],
    },
    {
        "name": "New Mexico",
        "slug": "new-mexico",
        "abbr": "NM",
        "population": "2.1 million",
        "region": "the Southwest",
        "center_count": "10+",
        "chains": ["CSL Plasma", "BioLife", "Octapharma", "Grifols"],
        "metros": ["Albuquerque", "Las Cruces", "Rio Rancho", "Santa Fe", "Roswell"],
        "top_cities": [
            ("Albuquerque", None),
            ("Las Cruces", None),
            ("Rio Rancho", None),
            ("Santa Fe", None),
        ],
    },
    {
        "name": "North Carolina",
        "slug": "north-carolina",
        "abbr": "NC",
        "population": "10.7 million",
        "region": "the Southeast",
        "center_count": "35+",
        "chains": ["CSL Plasma", "BioLife", "Octapharma", "Grifols"],
        "metros": ["Charlotte", "Raleigh", "Greensboro", "Durham", "Winston-Salem", "Fayetteville"],
        "top_cities": [
            ("Charlotte", None),
            ("Raleigh", None),
            ("Greensboro", None),
            ("Durham", None),
            ("Winston-Salem", None),
            ("Fayetteville", None),
        ],
    },
    {
        "name": "North Dakota",
        "slug": "north-dakota",
        "abbr": "ND",
        "population": "780,000",
        "region": "the Northern Plains",
        "center_count": "3-5",
        "chains": ["CSL Plasma", "BioLife"],
        "metros": ["Fargo", "Bismarck", "Grand Forks", "Minot"],
        "top_cities": [
            ("Fargo", None),
            ("Bismarck", None),
            ("Grand Forks", None),
        ],
    },
    {
        "name": "Ohio",
        "slug": "ohio",
        "abbr": "OH",
        "population": "11.8 million",
        "region": "the Midwest",
        "center_count": "45+",
        "chains": ["CSL Plasma", "BioLife", "Octapharma", "Grifols"],
        "metros": ["Columbus", "Cleveland", "Cincinnati", "Toledo", "Akron", "Dayton"],
        "top_cities": [
            ("Columbus", None),
            ("Cleveland", None),
            ("Cincinnati", None),
            ("Toledo", None),
            ("Akron", None),
            ("Dayton", None),
        ],
    },
    {
        "name": "Oklahoma",
        "slug": "oklahoma",
        "abbr": "OK",
        "population": "4.0 million",
        "region": "the South Central US",
        "center_count": "18+",
        "chains": ["CSL Plasma", "BioLife", "Octapharma", "Grifols"],
        "metros": ["Oklahoma City", "Tulsa", "Norman", "Broken Arrow", "Edmond", "Lawton"],
        "top_cities": [
            ("Oklahoma City", None),
            ("Tulsa", None),
            ("Norman", None),
            ("Broken Arrow", None),
            ("Lawton", None),
        ],
    },
    {
        "name": "Oregon",
        "slug": "oregon",
        "abbr": "OR",
        "population": "4.2 million",
        "region": "the Pacific Northwest",
        "center_count": "15+",
        "chains": ["CSL Plasma", "BioLife", "Octapharma", "Grifols"],
        "metros": ["Portland", "Salem", "Eugene", "Gresham", "Hillsboro", "Bend"],
        "top_cities": [
            ("Portland", None),
            ("Salem", None),
            ("Eugene", None),
            ("Bend", None),
            ("Hillsboro", None),
        ],
    },
    {
        "name": "Pennsylvania",
        "slug": "pennsylvania",
        "abbr": "PA",
        "population": "13.0 million",
        "region": "the Mid-Atlantic",
        "center_count": "40+",
        "chains": ["CSL Plasma", "BioLife", "Octapharma", "Grifols"],
        "metros": ["Philadelphia", "Pittsburgh", "Allentown", "Reading", "Erie", "Scranton"],
        "top_cities": [
            ("Philadelphia", None),
            ("Pittsburgh", None),
            ("Allentown", None),
            ("Reading", None),
            ("Erie", None),
            ("Scranton", None),
        ],
    },
    {
        "name": "Rhode Island",
        "slug": "rhode-island",
        "abbr": "RI",
        "population": "1.1 million",
        "region": "New England",
        "center_count": "3-4",
        "chains": ["CSL Plasma", "BioLife"],
        "metros": ["Providence", "Warwick", "Cranston"],
        "top_cities": [
            ("Providence", None),
            ("Warwick", None),
            ("Cranston", None),
        ],
    },
    {
        "name": "South Carolina",
        "slug": "south-carolina",
        "abbr": "SC",
        "population": "5.2 million",
        "region": "the Southeast",
        "center_count": "18+",
        "chains": ["CSL Plasma", "BioLife", "Octapharma", "Grifols"],
        "metros": ["Charleston", "Columbia", "North Charleston", "Greenville", "Rock Hill", "Mount Pleasant"],
        "top_cities": [
            ("Charleston", None),
            ("Columbia", None),
            ("Greenville", None),
            ("Rock Hill", None),
            ("Mount Pleasant", None),
        ],
    },
    {
        "name": "South Dakota",
        "slug": "south-dakota",
        "abbr": "SD",
        "population": "900,000",
        "region": "the Northern Plains",
        "center_count": "3-5",
        "chains": ["CSL Plasma", "BioLife"],
        "metros": ["Sioux Falls", "Rapid City", "Aberdeen"],
        "top_cities": [
            ("Sioux Falls", None),
            ("Rapid City", None),
            ("Aberdeen", None),
        ],
    },
    {
        "name": "Tennessee",
        "slug": "tennessee",
        "abbr": "TN",
        "population": "7.0 million",
        "region": "the Southeast",
        "center_count": "30+",
        "chains": ["CSL Plasma", "BioLife", "Octapharma", "Grifols"],
        "metros": ["Nashville", "Memphis", "Knoxville", "Chattanooga", "Clarksville", "Murfreesboro"],
        "top_cities": [
            ("Nashville", None),
            ("Memphis", None),
            ("Knoxville", None),
            ("Chattanooga", None),
            ("Clarksville", None),
        ],
    },
    {
        "name": "Utah",
        "slug": "utah",
        "abbr": "UT",
        "population": "3.4 million",
        "region": "the Mountain West",
        "center_count": "15+",
        "chains": ["CSL Plasma", "BioLife", "Octapharma", "Grifols"],
        "metros": ["Salt Lake City", "West Valley City", "Provo", "West Jordan", "Orem", "Sandy"],
        "top_cities": [
            ("Salt Lake City", None),
            ("West Valley City", None),
            ("Provo", None),
            ("Orem", None),
            ("Sandy", None),
        ],
    },
    {
        "name": "Vermont",
        "slug": "vermont",
        "abbr": "VT",
        "population": "647,000",
        "region": "New England",
        "center_count": "1-2",
        "chains": ["CSL Plasma"],
        "metros": ["Burlington", "South Burlington", "Rutland"],
        "top_cities": [
            ("Burlington", None),
            ("South Burlington", None),
        ],
    },
    {
        "name": "Virginia",
        "slug": "virginia",
        "abbr": "VA",
        "population": "8.6 million",
        "region": "the Mid-Atlantic / Southeast",
        "center_count": "25+",
        "chains": ["CSL Plasma", "BioLife", "Octapharma", "Grifols"],
        "metros": ["Virginia Beach", "Norfolk", "Chesapeake", "Richmond", "Arlington", "Newport News", "Alexandria"],
        "top_cities": [
            ("Virginia Beach", None),
            ("Norfolk", None),
            ("Richmond", None),
            ("Arlington", None),
            ("Chesapeake", None),
            ("Newport News", None),
        ],
    },
    {
        "name": "Washington",
        "slug": "washington",
        "abbr": "WA",
        "population": "7.8 million",
        "region": "the Pacific Northwest",
        "center_count": "25+",
        "chains": ["CSL Plasma", "BioLife", "Octapharma", "Grifols"],
        "metros": ["Seattle", "Spokane", "Tacoma", "Vancouver", "Bellevue", "Kent"],
        "top_cities": [
            ("Seattle", None),
            ("Spokane", None),
            ("Tacoma", None),
            ("Vancouver", None),
            ("Bellevue", None),
        ],
    },
    {
        "name": "West Virginia",
        "slug": "west-virginia",
        "abbr": "WV",
        "population": "1.8 million",
        "region": "Appalachia",
        "center_count": "8+",
        "chains": ["CSL Plasma", "BioLife", "Grifols"],
        "metros": ["Charleston", "Huntington", "Morgantown", "Parkersburg", "Wheeling"],
        "top_cities": [
            ("Charleston", None),
            ("Huntington", None),
            ("Morgantown", None),
            ("Parkersburg", None),
        ],
    },
    {
        "name": "Wisconsin",
        "slug": "wisconsin",
        "abbr": "WI",
        "population": "5.9 million",
        "region": "the Upper Midwest",
        "center_count": "20+",
        "chains": ["CSL Plasma", "BioLife", "Octapharma", "Grifols"],
        "metros": ["Milwaukee", "Madison", "Green Bay", "Kenosha", "Racine", "Appleton"],
        "top_cities": [
            ("Milwaukee", None),
            ("Madison", None),
            ("Green Bay", None),
            ("Kenosha", None),
            ("Appleton", None),
        ],
    },
    {
        "name": "Wyoming",
        "slug": "wyoming",
        "abbr": "WY",
        "population": "577,000",
        "region": "the Mountain West",
        "center_count": "1-2",
        "chains": ["CSL Plasma"],
        "metros": ["Cheyenne", "Casper", "Laramie"],
        "top_cities": [
            ("Cheyenne", None),
            ("Casper", None),
        ],
    },
]


def build_chains_table(chains):
    """Build HTML table rows for chains operating in the state."""
    chain_data = {
        "CSL Plasma": ("$50-$100", "$700-$1,200", "$400-$1,000"),
        "BioLife": ("$60-$100", "$900-$1,100", "$400-$900"),
        "Octapharma": ("$50-$85", "$800-$1,000", "$450-$900"),
        "Grifols": ("$50-$75", "$700-$1,100", "$400-$900"),
    }
    rows = ""
    for chain in chains:
        pay, bonus, monthly = chain_data[chain]
        link_slug = {
            "CSL Plasma": "csl-plasma-pay-rates-2026",
            "BioLife": "biolife-plasma-pay-rates-2026",
            "Octapharma": "octapharma-plasma-pay-rates-2026",
            "Grifols": "grifols-plasma-pay-rates-2026",
        }[chain]
        rows += f'<tr><td><a href="/blog/{link_slug}.html" style="color: #0d9488; font-weight: 500;">{chain}</a></td><td>{pay}</td><td>{bonus}</td><td>{monthly}</td></tr>\n'
    return rows


def build_cities_list(top_cities, state_name):
    """Build HTML list of top cities with links where available."""
    items = ""
    for city, link in top_cities:
        if link:
            items += f'<li><a href="{link}" style="color: #0d9488; font-weight: 500;">{city}</a> — Multiple plasma centers with competitive pay rates</li>\n'
        else:
            items += f'<li><strong>{city}</strong> — Plasma donation centers available for local donors</li>\n'
    return items


def generate_state_page(state):
    """Generate a single state-level plasma center guide page."""
    name = state["name"]
    slug = f"best-plasma-centers-{state['slug']}-2026"
    abbr = state["abbr"]
    population = state["population"]
    region = state["region"]
    center_count = state["center_count"]
    chains = state["chains"]
    metros = state["metros"]
    top_cities = state["top_cities"]

    title = f"Best Plasma Donation Centers in {name} 2026: Pay Rates & Locations"
    meta_desc = (
        f"Find the best plasma donation centers in {name} for 2026. "
        f"Compare pay rates at {', '.join(chains[:3])} across {', '.join(metros[:3])}. "
        f"New donor bonuses up to $1,100."
    )
    category = f"{name} Plasma Centers"
    read_time = 9

    toc = [
        ("quick-answer", "Quick Answer"),
        ("overview", f"{name} Overview"),
        ("centers", "Center Comparison"),
        ("pay-rates", "Pay Rates by Weight"),
        ("cities", f"Top Cities in {name}"),
        ("new-donor", "New Donor Bonuses"),
        ("tips", "Local Tips"),
        ("faq", "FAQ"),
    ]

    metros_str = ", ".join(metros[:5])
    chains_str = ", ".join(chains)
    chain_rows = build_chains_table(chains)
    city_items = build_cities_list(top_cities, name)

    # Determine chain availability note
    if len(chains) == 4:
        chain_note = f"All four major national plasma center chains operate in {name}, giving donors plenty of options to compare pay rates."
    elif len(chains) >= 2:
        chain_note = f"{name} is served by {chains_str}. Donors may need to travel to nearby metro areas for the best selection of centers."
    else:
        chain_note = f"Plasma center options in {name} are more limited, with {chains_str} being the primary {'chain' if len(chains) == 1 else 'chains'} operating in the state. Consider checking neighboring states for additional options."

    content = f'''
<div class="highlight-box" id="quick-answer"><h3>Quick Answer</h3><p><strong>{name}</strong> has {center_count} plasma donation centers across the state, concentrated in metro areas like {metros_str}. New donors can earn <strong>$700-$1,100 in their first month</strong> through promotional bonuses. Regular donors earn <strong>$400-$900 per month</strong> donating twice weekly. The major chains operating here include {chains_str}.</p></div>

<h2 id="overview">{name} Plasma Donation Overview</h2>
<p>With a population of {population}, {name} is located in {region} and offers {center_count} plasma donation centers across its major metro areas. Whether you live in {metros[0]}, {metros[1] if len(metros) > 1 else metros[0]}, or {metros[2] if len(metros) > 2 else metros[0]}, there are plasma centers nearby where you can earn extra income while helping save lives.</p>
<ul>
<li><strong>Population:</strong> {population}</li>
<li><strong>Major Metros:</strong> {metros_str}</li>
<li><strong>Plasma Centers Statewide:</strong> {center_count}</li>
<li><strong>Major Chains:</strong> {chains_str}</li>
<li><strong>Average Monthly Earnings:</strong> $400-$900 (regular donors)</li>
</ul>
<p>{chain_note}</p>

<h2 id="centers">Plasma Center Comparison in {name}</h2>
<p>Here is a comparison of the major plasma center chains operating in {name}. Pay rates can vary by location, donor weight, and current promotions, so always verify with your local center.</p>

<table><thead><tr><th>Center Chain</th><th>Pay Per Visit</th><th>New Donor Bonus</th><th>Monthly Potential</th></tr></thead><tbody>
{chain_rows}</tbody></table>

<p>Pay rates shown are typical ranges across {name} locations. Individual centers may offer higher or lower rates depending on local demand, seasonal promotions, and your donor profile (weight, frequency).</p>

{AFFILIATE_BLOCK}

<h2 id="pay-rates">Plasma Donation Pay Rates by Weight in {name}</h2>
<p>All plasma centers pay based on your body weight because heavier donors can safely give more plasma per session. Here are the typical pay ranges at {name} plasma centers:</p>

<table><thead><tr><th>Weight Range</th><th>Plasma Volume</th><th>Pay Per Visit</th><th>Monthly (8 visits)</th></tr></thead><tbody>
<tr><td>110-149 lbs</td><td>690-825 mL</td><td>$50-$70</td><td>$400-$560</td></tr>
<tr><td>150-174 lbs</td><td>825 mL</td><td>$60-$85</td><td>$480-$680</td></tr>
<tr><td>175-400 lbs</td><td>880 mL</td><td>$75-$125</td><td>$600-$1,000</td></tr>
</tbody></table>

<p>Higher weight donors (175+ lbs) earn significantly more because they can donate larger plasma volumes. The second donation each week typically pays more than the first as an incentive for twice-weekly visits.</p>

<h2 id="cities">Top Cities for Plasma Donation in {name}</h2>
<p>Here are the best cities in {name} to find plasma donation centers with competitive pay rates:</p>

<ul>
{city_items}</ul>

<p>Use our <a href="/centers/" style="color: #0d9488; font-weight: 500;">Center Finder</a> to locate the nearest plasma center in {name} and compare current pay rates at each location.</p>

<h2 id="new-donor">New Donor Bonuses in {name}</h2>
<p>First-time plasma donors in {name} can take advantage of generous new donor bonus programs offered by major chains. These promotions typically require completing 6-8 donations within your first 30-45 days.</p>

<table><thead><tr><th>Center</th><th>New Donor Bonus</th><th>Bonus Period</th><th>Requirements</th></tr></thead><tbody>
<tr><td>CSL Plasma</td><td>$700-$1,200</td><td>First 30-45 days</td><td>6-8 donations</td></tr>
<tr><td>BioLife</td><td>$900-$1,100</td><td>First 30 days</td><td>8 donations</td></tr>
<tr><td>Octapharma</td><td>$800-$1,000</td><td>First 30 days</td><td>6-8 donations</td></tr>
<tr><td>Grifols</td><td>$700-$1,100</td><td>First 45 days</td><td>6-8 donations</td></tr>
</tbody></table>

<p><strong>Pro Tip:</strong> New donor bonuses change monthly. Before your first visit, check each center\'s website or call ahead to confirm current promotions in your {name} location.</p>

{PRO_TOOLKIT}

<h2 id="tips">Local Tips for {name} Plasma Donors</h2>
<p>Here are some state-specific tips to help you maximize your plasma donation earnings in {name}:</p>
<ol>
<li><strong>Compare multiple centers</strong> — With {center_count} centers across {name}, take time to compare pay rates at different locations before committing. Even centers of the same chain can offer different promotional rates.</li>
<li><strong>Time your visits</strong> — Many {name} donors report shorter wait times early in the morning or mid-week (Tuesday-Thursday). Avoid peak times on Mondays and Fridays.</li>
<li><strong>Stack new donor bonuses</strong> — Complete all required donations within the bonus period to maximize your first-month earnings. Missing even one visit could reduce your total payout.</li>
<li><strong>Stay hydrated</strong> — {region.replace("the ", "").title()} weather can affect hydration levels. Drink at least 64 oz of water the day before donating to ensure a smooth, fast donation.</li>
<li><strong>Use referral programs</strong> — Most centers offer $50-$100 per successful referral. Share your referral code with friends and family in {metros[0]} and surrounding areas.</li>
<li><strong>Download the app</strong> — CSL Plasma, BioLife, and Octapharma all have mobile apps for scheduling appointments, checking balances, and finding the latest promotions at {name} locations.</li>
</ol>

{related_reading([
    ("/blog/which-plasma-center-pays-most-money.html", "Which Plasma Center Pays the Most Money?"),
    ("/blog/ultimate-first-time-plasma-donor-guide-2026.html", "Ultimate First-Time Plasma Donor Guide"),
    ("/", "Plasma Pay Calculator"),
    ("/blog/plasma-donation-weight-chart-2026.html", "Plasma Donation Weight Chart 2026"),
])}

<h2 id="faq">Frequently Asked Questions</h2>

<h3>What is the highest paying plasma center in {name}?</h3>
<p>CSL Plasma and BioLife typically offer the highest pay rates in {name}, with new donor bonuses of $700-$1,200 in the first month. Regular donors earn $50-$125 per visit depending on weight and location. Use our <a href="/">Plasma Pay Calculator</a> to estimate your exact earnings.</p>

<h3>How much can you make donating plasma in {name}?</h3>
<p>{name} plasma donors can earn $400-$1,000+ per month donating twice weekly. New donors earn significantly more in their first month through promotional bonuses, typically $700-$1,100 at major centers across {metros[0]} and other cities.</p>

<h3>How many plasma centers are there in {name}?</h3>
<p>{name} has {center_count} plasma donation centers across the state, operated by {chains_str}. The highest concentration of centers is found in {metros[0]} and {metros[1] if len(metros) > 1 else "surrounding suburbs"}.</p>

<h3>What are the requirements to donate plasma in {name}?</h3>
<p>To donate plasma in {name}, you must be 18-69 years old, weigh at least 110 lbs, have a valid photo ID, Social Security proof, and proof of current address. You must pass a medical screening and physical exam on your first visit. Specific requirements may vary by center.</p>

{footer_related()}'''

    faqs = [
        make_faq(
            f"What is the highest paying plasma center in {name}?",
            f"CSL Plasma and BioLife typically offer the highest pay rates in {name}, with new donor bonuses of $700-$1,200 in the first month. Regular donors earn $50-$125 per visit depending on weight and location."
        ),
        make_faq(
            f"How much can you make donating plasma in {name}?",
            f"{name} plasma donors can earn $400-$1,000+ per month donating twice weekly. New donors earn $700-$1,100 in their first month through bonus programs."
        ),
        make_faq(
            f"How many plasma centers are there in {name}?",
            f"{name} has {center_count} plasma donation centers across the state, operated by {chains_str}."
        ),
        make_faq(
            f"What are the requirements to donate plasma in {name}?",
            f"You must be 18-69 years old, weigh at least 110 lbs, have a valid photo ID, Social Security proof, and proof of current address. You must pass a medical screening on your first visit."
        ),
    ]

    html = make_en_page(slug, title, meta_desc, category, read_time, toc, content, faqs)
    filepath = os.path.join(BLOG_DIR, f"{slug}.html")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  Created: blog/{slug}.html")
    return slug


if __name__ == '__main__':
    print(f"Generating Round 3: State-Level Plasma Center Guide Pages ({len(STATES)} states)...")
    print(f"Output directory: {BLOG_DIR}")
    print()

    created = []
    for state in STATES:
        slug = generate_state_page(state)
        created.append(slug)

    print()
    print(f"Done! Generated {len(created)} state-level guide pages.")
    print()
    print("States created:")
    for i, slug in enumerate(created, 1):
        print(f"  {i:2d}. {slug}.html")
