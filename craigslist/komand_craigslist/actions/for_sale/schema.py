# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Search the for sale section"


class Input:
    CATEGORY = "category"
    HAS_IMAGE = "has_image"
    POSTED_TODAY = "posted_today"
    QUERY = "query"
    SEARCH_DISTANCE = "search_distance"
    SEARCH_TITLES = "search_titles"
    SECTION_FILTER = "section_filter"
    SITE = "site"
    ZIP_CODE = "zip_code"
    

class Output:
    SALE_POSTING = "sale_posting"
    

class ForSaleInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "category": {
      "type": "string",
      "title": "Category",
      "description": "Craigslist sales category",
      "enum": [
        "antiques",
        "appliances",
        "arts+crafts",
        "atv/utv/sno",
        "auto parts",
        "baby+kids",
        "barter",
        "beauty+hlth",
        "bikes",
        "boats",
        "books",
        "business",
        "cars+trucks",
        "cds/dvd/vhs",
        "cell phones",
        "clothes+acc",
        "collectibles",
        "computers",
        "electronics",
        "farm+garden",
        "free",
        "furniture",
        "garage sale",
        "general",
        "heavy equip",
        "household",
        "jewelry",
        "materials",
        "motorcycles",
        "music instr",
        "photo+video",
        "rvs+camp",
        "sporting",
        "tickets",
        "tools",
        "toys+games",
        "trailers",
        "video gaming",
        "wanted"
      ],
      "order": 2
    },
    "has_image": {
      "type": "boolean",
      "title": "Has Image",
      "description": "Posting contains an image",
      "default": false,
      "order": 5
    },
    "posted_today": {
      "type": "boolean",
      "title": "Posted Today",
      "description": "Is posted today",
      "default": false,
      "order": 4
    },
    "query": {
      "type": "string",
      "title": "Query",
      "description": "Query string",
      "order": 6
    },
    "search_distance": {
      "type": "integer",
      "title": "Search Distance",
      "description": "Search distance in miles",
      "order": 7
    },
    "search_titles": {
      "type": "boolean",
      "title": "Search Titles",
      "description": "Search the titles",
      "default": false,
      "order": 3
    },
    "section_filter": {
      "type": "object",
      "title": "Section Filter",
      "description": "Craigslist has specific filters for each category. You can fine tune your search by entering a section specific filter as JSON e.g. { \\"max_price\\": 5000, \\"auto_size\\": \\"compact\\", \\"auto_paint\\": \\"blue\\" }",
      "order": 9
    },
    "site": {
      "type": "string",
      "title": "Site",
      "description": "Craigslist site location",
      "enum": [
        "columbusga",
        "monterey",
        "buenosaires",
        "cincinnati",
        "guelph",
        "kamloops",
        "merced",
        "nottingham",
        "brantford",
        "stgeorge",
        "roanoke",
        "oslo",
        "venice",
        "lille",
        "bismarck",
        "farmington",
        "wyoming",
        "kootenays",
        "sanantonio",
        "pampanga",
        "curitiba",
        "columbiamo",
        "appleton",
        "delhi",
        "chennai",
        "sherbrooke",
        "tulsa",
        "wausa,",
        "nanaimo",
        "muskegon",
        "southjersey",
        "dothan",
        "limaohio",
        "syracuse",
        "pueblo",
        "norfolk",
        "brisbane",
        "puebla",
        "cenla",
        "alicante",
        "plattsburgh",
        "mumbai",
        "bozeman",
        "mattoon",
        "cfl",
        "siouxcity",
        "lascruces",
        "panamacity",
        "quebec",
        "rouen",
        "copenhagen",
        "augusta",
        "princegeorge",
        "newjersey",
        "panama",
        "rockies",
        "greenville",
        "annarbor",
        "richmond",
        "taipei",
        "northmiss",
        "fortlauderdale",
        "racine",
        "canarias",
        "siouxfalls",
        "harrisonburg",
        "sarasota",
        "capetown",
        "guangzho,",
        "okinawa",
        "wuhan",
        "leeds",
        "hobart",
        "newlondon",
        "morgantown",
        "chongqing",
        "ukraine",
        "bakersfield",
        "spokane",
        "juarez",
        "lucknow",
        "grandforks",
        "dublin",
        "elpaso",
        "hiroshima",
        "paris",
        "christchurch",
        "derby",
        "capecod",
        "brownsville",
        "saguenay",
        "shanghai",
        "stockton",
        "montpellier",
        "sicily",
        "nanjing",
        "lima",
        "florence",
        "monterrey",
        "onslow",
        "battlecreek",
        "quadcities",
        "territories",
        "eastmids",
        "calgary",
        "corvallis",
        "brunswick",
        "sarnia",
        "wenatchee",
        "centralmich",
        "tuscarawas",
        "glensfalls",
        "asheville",
        "mansfield",
        "saltlakecity",
        "ahmedabad",
        "tampa",
        "rockford",
        "visalia",
        "siskiyo,",
        "salvador",
        "tokyo",
        "sanangelo",
        "blacksburg",
        "delrio",
        "lakecharles",
        "montevideo",
        "westky",
        "pretoria",
        "newfoundland",
        "beijing",
        "texarkana",
        "norwich",
        "niagara",
        "bend",
        "acapulco",
        "athensga",
        "newhaven",
        "csd",
        "torino",
        "hampshire",
        "showlow",
        "louisville",
        "catskills",
        "vancouver",
        "kolkata",
        "inlandempire",
        "chillicothe",
        "springfield",
        "bajasur",
        "edinburgh",
        "seoul",
        "mankato",
        "faro",
        "goldcoast",
        "sardinia",
        "swks",
        "charleston",
        "billings",
        "southcoast",
        "joplin",
        "mendocino",
        "hannover",
        "killeen",
        "guatemala",
        "corpuschristi",
        "sendai",
        "lubbock",
        "tijuana",
        "yubasutter",
        "sd",
        "galveston",
        "houston",
        "tallahassee",
        "casablanca",
        "canberra",
        "fresno",
        "beaumont",
        "washingtondc",
        "auburn",
        "helena",
        "logan",
        "modesto",
        "milwaukee",
        "sapporo",
        "chihuahua",
        "thumb",
        "fairbanks",
        "oneonta",
        "denver",
        "klamath",
        "winnipeg",
        "charlottesville",
        "portoalegre",
        "meridian",
        "eugene",
        "poconos",
        "manila",
        "zagreb",
        "myrtlebeach",
        "stcloud",
        "harrisburg",
        "stjoseph",
        "oxford",
        "bath",
        "porto",
        "kpr",
        "susanville",
        "hickory",
        "yellowknife",
        "missoula",
        "detroit",
        "eastky",
        "saopaulo",
        "stockholm",
        "surat",
        "rennes",
        "redding",
        "genoa",
        "medford",
        "zurich",
        "cairo",
        "osaka",
        "milan",
        "portland",
        "eastnc",
        "albanyga",
        "hongkong",
        "jerusalem",
        "jackson",
        "fortsmith",
        "goldcountry",
        "kuwait",
        "texoma",
        "pensacola",
        "goa",
        "hangzho,",
        "mazatlan",
        "terrehaute",
        "kent",
        "bacolod",
        "fargo",
        "smd",
        "florencesc",
        "quito",
        "durban",
        "lawrence",
        "sfbay",
        "sheffield",
        "albuquerque",
        "york",
        "shreveport",
        "scottsbluff",
        "chatham",
        "lynchburg",
        "pune",
        "desmoines",
        "waterloo",
        "cadiz",
        "dunedin",
        "bilbao",
        "belleville",
        "raleigh",
        "cotedazur",
        "santamaria",
        "lewiston",
        "austin",
        "lasalle",
        "macon",
        "hyderabad",
        "toulouse",
        "humboldt",
        "neworleans",
        "roswell",
        "bham",
        "shenyang",
        "olympic",
        "colombia",
        "cedarrapids",
        "enid",
        "gulfport",
        "strasbourg",
        "guanajuato",
        "bologna",
        "sandusky",
        "charlestonwv",
        "danville",
        "muncie",
        "geneva",
        "pittsburgh",
        "peoria",
        "vermont",
        "cornwall",
        "hartford",
        "honolul,",
        "valencia",
        "tehran",
        "eauclaire",
        "rapidcity",
        "malaga",
        "toronto",
        "evansville",
        "holland",
        "richmondin",
        "helsinki",
        "youngstown",
        "ventura",
        "lausanne",
        "tunis",
        "prescott",
        "vienna",
        "charlotte",
        "dalian",
        "costarica",
        "boston",
        "sevilla",
        "shoals",
        "worcester",
        "reno",
        "wellington",
        "tuscaloosa",
        "junea,",
        "jaipur",
        "windsor",
        "brighton",
        "warsaw",
        "rochester",
        "abilene",
        "parkersburg",
        "wichitafalls",
        "martinsburg",
        "montgomery",
        "eastco",
        "clovis",
        "beirut",
        "yakima",
        "santafe",
        "santiago",
        "dayton",
        "victoria",
        "liverpool",
        "montana",
        "littlerock",
        "owensound",
        "haifa",
        "omaha",
        "gadsden",
        "mobile",
        "hanford",
        "seks",
        "chicago",
        "frederick",
        "kaiserslautern",
        "lakecity",
        "istanbul",
        "bordeaux",
        "loire",
        "madison",
        "bellingham",
        "cdo",
        "victoriatx",
        "manchester",
        "nagoya",
        "naga",
        "baleares",
        "westmd",
        "maine",
        "staugustine",
        "ks,",
        "ceb,",
        "greenbay",
        "treasure",
        "basel",
        "cookeville",
        "lansing",
        "perugia",
        "darwin",
        "boulder",
        "ftmcmurray",
        "palmsprings",
        "baghdad",
        "fayar",
        "nwga",
        "lethbridge",
        "budapest",
        "wilmington",
        "lexington",
        "kirksville",
        "london",
        "recife",
        "wheeling",
        "kitchener",
        "bulgaria",
        "kalamazoo",
        "twintiers",
        "reykjavik",
        "prague",
        "cologne",
        "cairns",
        "longisland",
        "lisbon",
        "roseburg",
        "rmn",
        "fortdodge",
        "hattiesburg",
        "lancaster",
        "lyon",
        "ocala",
        "knoxville",
        "londonon",
        "dundee",
        "newyork",
        "toledo",
        "reading",
        "glasgow",
        "yuma",
        "losangeles",
        "stlouis",
        "nashville",
        "boise",
        "wv",
        "akroncanton",
        "grandrapids",
        "butte",
        "ames",
        "bangkok",
        "indore",
        "winchester",
        "leipzig",
        "saskatoon",
        "ntl",
        "stuttgart",
        "bristol",
        "statesboro",
        "lawton",
        "hiltonhead",
        "baltimore",
        "pakistan",
        "westslope",
        "moscow",
        "owensboro",
        "meadville",
        "masoncity",
        "santodomingo",
        "kerala",
        "pv",
        "reddeer",
        "kokomo",
        "hamilton",
        "sierravista",
        "fortaleza",
        "bhubaneswar",
        "naples",
        "ramallah",
        "odessa",
        "chandigarh",
        "kingston",
        "huntsville",
        "sunshine",
        "nwct",
        "williamsport",
        "hamburg",
        "atlanta",
        "stillwater",
        "sandiego",
        "oklahomacity",
        "coventry",
        "brasilia",
        "mohave",
        "valdosta",
        "natchez",
        "bemidji",
        "addisababa",
        "slo",
        "northplatte",
        "xian",
        "elmira",
        "rio",
        "barcelona",
        "kenya",
        "seattle",
        "monroe",
        "outerbanks",
        "albany",
        "salina",
        "kelowna",
        "managua",
        "kalispell",
        "comoxvalley",
        "annapolis",
        "guadalajara",
        "zamboanga",
        "jacksontn",
        "bigbend",
        "utica",
        "ashtabula",
        "carbondale",
        "adelaide",
        "chautauqua",
        "indianapolis",
        "columbia",
        "singapore",
        "zanesville",
        "keys",
        "sacramento",
        "houma",
        "sheboygan",
        "nesd",
        "brussels",
        "caracas",
        "lacrosse",
        "chattanooga",
        "daytona",
        "dallas",
        "iowacity",
        "porthuron",
        "rome",
        "montreal",
        "flint",
        "ottumwa",
        "aberdeen",
        "savannah",
        "nd",
        "edmonton",
        "winstonsalem",
        "abbotsford",
        "birmingham",
        "hermosillo",
        "auckland",
        "mcallen",
        "ithaca",
        "belfast",
        "fortwayne",
        "fukuoka",
        "clarksville",
        "micronesia",
        "newbrunswick",
        "santabarbara",
        "perth",
        "cosprings",
        "sydney",
        "hat",
        "heidelberg",
        "springfieldil",
        "grandisland",
        "chambersburg",
        "dubai",
        "munich",
        "amarillo",
        "newcastle",
        "jonesboro",
        "grenoble",
        "jacksonville",
        "davaocity",
        "semo",
        "lincoln",
        "moseslake",
        "saginaw",
        "miami",
        "orlando",
        "dusseldorf",
        "johannesburg",
        "veracruz",
        "duluth",
        "oaxaca",
        "accra",
        "jxn",
        "chico",
        "bucharest",
        "brainerd",
        "madrid",
        "elko",
        "malaysia",
        "altoona",
        "athens",
        "lapaz",
        "cleveland",
        "halifax",
        "batonrouge",
        "regina",
        "wollongong",
        "delaware",
        "luxembourg",
        "marseilles",
        "whitehorse",
        "providence",
        "caribbean",
        "pei",
        "cnj",
        "columbus",
        "dresden",
        "bgky",
        "bn",
        "swva",
        "northernwi",
        "binghamton",
        "barrie",
        "bangalore",
        "decatur",
        "nmi",
        "anchorage",
        "collegestation",
        "sanmarcos",
        "melbourne",
        "topeka",
        "whistler",
        "greatfalls",
        "fingerlakes",
        "greensboro",
        "skagit",
        "fortcollins",
        "cambridge",
        "chengd,",
        "marshall",
        "fredericksburg",
        "essex",
        "soo",
        "provo",
        "cardiff",
        "amsterdam",
        "essen",
        "pullman",
        "twinfalls",
        "kansascity",
        "nwks",
        "bangladesh",
        "waco",
        "chambana",
        "philadelphia",
        "imperial",
        "virgin",
        "stpetersburg",
        "tippecanoe",
        "loz",
        "bloomington",
        "lasvegas",
        "mexicocity",
        "laredo",
        "athensohio",
        "monroemi",
        "easttexas",
        "troisrivieres",
        "iloilo",
        "swmi",
        "bern",
        "memphis",
        "flagstaff",
        "nuremberg",
        "cariboo",
        "skeena",
        "jerseyshore",
        "up",
        "puertorico",
        "tucson",
        "jakarta",
        "swv",
        "ogden",
        "sudbury",
        "southbend",
        "okaloosa",
        "wichita",
        "janesville",
        "minneapolis",
        "belohorizonte",
        "salem",
        "ottawa",
        "erie",
        "hudsonvalley",
        "huntington",
        "eastidaho",
        "nh",
        "pennstate",
        "granada",
        "peterborough",
        "elsalvador",
        "allentown",
        "peace",
        "gainesville",
        "bremen",
        "telaviv",
        "potsdam",
        "thunderbay",
        "yucatan",
        "easternshore",
        "shenzhen",
        "nacogdoches",
        "phoenix",
        "dubuque",
        "devon",
        "eastoregon",
        "kenai",
        "quincy",
        "orangecounty",
        "fortmyers",
        "westernmass",
        "scranton",
        "frankfurt",
        "lakeland",
        "berlin",
        "spacecoast",
        "watertown",
        "vietnam",
        "lafayette",
        "boone",
        "oregoncoast",
        "fayetteville",
        "tricities",
        "buffalo"
      ],
      "order": 1
    },
    "zip_code": {
      "type": "integer",
      "title": "Zip Code",
      "description": "Zipcode",
      "order": 8
    }
  },
  "required": [
    "category",
    "site"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ForSaleOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "sale_posting": {
      "type": "array",
      "title": "Sale  Posting",
      "description": "Item posting information",
      "items": {
        "$ref": "#/definitions/sale_posting"
      },
      "order": 1
    }
  },
  "definitions": {
    "sale_posting": {
      "type": "object",
      "title": "sale_posting",
      "properties": {
        "datetime": {
          "type": "string",
          "title": "DateTime",
          "description": "Posting Date/Time",
          "order": 9
        },
        "geotag": {
          "type": "string",
          "title": "Geotag",
          "order": 6
        },
        "has_image": {
          "type": "boolean",
          "title": "Has Image",
          "description": "Posting includes an image",
          "order": 2
        },
        "has_map": {
          "type": "boolean",
          "title": "Has Map",
          "description": "Posting includes a map",
          "order": 3
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "Posting ID",
          "order": 8
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Item name",
          "order": 1
        },
        "price": {
          "type": "string",
          "title": "Price",
          "description": "Item price",
          "order": 5
        },
        "url": {
          "type": "string",
          "title": "Url",
          "description": "Posting URL",
          "order": 4
        },
        "where": {
          "type": "string",
          "title": "Where",
          "description": "Address",
          "order": 7
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
