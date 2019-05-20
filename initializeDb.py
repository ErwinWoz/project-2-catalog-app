import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Categories, Items

# create an engine and start interacting with databases
engine = create_engine('sqlite:///catalog.db')

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

# create "DBSession" class to converse with database
# create an instance of a DBSession class
DBSession = sessionmaker(bind=engine)
db_session = DBSession()


Items for caregory1(Soccer)
category1 = Categories(name="Soccer")
db_session.add(category1)
db_session.commit()

soccerItem1 = Items(title="Soccer Ball",
                    description="The standard soccer ball is made of synthetic\
                    leather, usually polyurethane or polyvinyl chloride,\
                    stitched around an inflated rubber or rubber-like\
                    bladder. Older balls were made of genuine leather and held\
                    shut with cotton laces. Modern balls have a valve.",
                    updated=datetime.datetime.now(),
                    categories=category1)
db_session.add(soccerItem1)
db_session.commit()

soccerItem2 = Items(title="Cleats",
                    description="Football boots, called cleats or soccer shoes\
                    in North America, are an item of footwear worn when\
                    playing football. Those designed for grass pitches have\
                    studs on the outsole to aid grip.",
                    updated=datetime.datetime.now(),
                    categories=category1)
db_session.add(soccerItem2)
db_session.commit()

soccerItem3 = Items(title="Goalkeeper gloves",
                    description="Goalkeeper gloves provide a better grip on\
                    the ball, protect and cushion your fingers and palms, and\
                    help you block, catch and punch the ball. Goalkeeper\
                    gloves are usually made from a blend of natural and\
                    synthetic latex foams.",
                    updated=datetime.datetime.now(),
                    categories=category1)
db_session.add(soccerItem3)
db_session.commit()

soccerItem4 = Items(title="Shin guards",
                    description="A shin guard is a thick piece of material\
                    that you wear inside your socks to protect the lower part\
                    of your leg when you are playing a game such as soccer.",
                    updated=datetime.datetime.now(),
                    categories=category1)
db_session.add(soccerItem4)
db_session.commit()

soccerItem5 = Items(title="Goal",
                    description=" A goal is a physical structure or area where\
                    an attacking team must send the ball in order to score\
                    points. In soccer, a goal is the sole method of scoring,\
                    and thus the final score is expressed in the total number\
                    of goals scored by each team.",
                    updated=datetime.datetime.now(),
                    categories=category1)
db_session.add(soccerItem5)
db_session.commit()


# Items for caregory2(Snowboarding)
category2 = Categories(name="Snowboarding")
db_session.add(category2)
db_session.commit()

snowboardItem1 = Items(title="Helmet",
                       description="A helmet is a form of protective gear worn to\
                       protect the head. More specifically, a helmet\
                       complements the skull in protecting the human brain.\
                       Helmets are available in many styles, and typically\
                       consist of a hard plastic/resin shell with inner\
                       padding.",
                       updated=datetime.datetime.now(),
                       categories=category2)
db_session.add(snowboardItem1)
db_session.commit()

snowboardItem2 = Items(title="Gloves",
                       description="Snowboard gloves are are a key component to\
                       staying warm, dry, and happy on the mountain. Gloves\
                       for snowboarding offer a distinct advantage over\
                       mittens - dexterity and finger functionality.\
                       Splitting up your fingers makes things like strapping\
                       into snowboard bindings and pulling on zippers that\
                       much easier.",
                       updated=datetime.datetime.now(),
                       categories=category2)
db_session.add(snowboardItem2)
db_session.commit()

snowboardItem3 = Items(title="Boots",
                       description="Snowboard boots are mostly considered soft\
                       boots, though alpine snowboarding uses a harder boot\
                       similar to a ski boot. A boot's primary function is to\
                       transfer the rider's energy into the board, protect the\
                       rider with support, and keep the rider's feet warm. A\
                       snowboarder shopping for boots is usually looking for a\
                       good fit, flex, and looks.",
                       updated=datetime.datetime.now(),
                       categories=category2)
db_session.add(snowboardItem3)
db_session.commit()

snowboardItem4 = Items(title="Goggles",
                       description="Snowboard goggles are an important piece of\
                       kit. They protect your eyes from the elements, such as\
                       snow, wind, and harmful UV rays, while improving your\
                       vision so that you get to see the mountain as well as\
                       possible.",
                       updated=datetime.datetime.now(),
                       categories=category2)
db_session.add(snowboardItem4)
db_session.commit()

snowboardItem5 = Items(title="Snowboard",
                       description="Snowboard is boards where both feet are\
                       secured to the same board, which are wider than skis,\
                       with the ability to glide on snow. Snowboards widths\
                       are between 6 and 12 inches or 15 to 30 centimeters.",
                       updated=datetime.datetime.now(),
                       categories=category2)
db_session.add(snowboardItem5)
db_session.commit()


# Items for caregory3(Rock Climbing)
category3 = Categories(name="Rock Climbing")
db_session.add(category3)
db_session.commit()

climbItem1 = Items(title="Carabiners",
                   description="Carabiners are metal loops with spring-loaded\
                    gates (openings), used as connectors. Once made primarily\
                    from steel, almost all carabiners for recreational\
                    climbing are now made from a light weight aluminum alloy.\
                    Steel carabiners are much heavier, but harder wearing, and\
                    therefore are often used by instructors when working with\
                    groups",
                   updated=datetime.datetime.now(),
                   categories=category3)
db_session.add(climbItem1)
db_session.commit()

climbItem2 = Items(title="Quickdraws",
                   description="Quickdraws (often referred to as 'draws') are\
                    used by climbers to connect ropes to bolt anchors, or to\
                    other traditional protection, allowing the rope to move\
                    through the anchoring system with minimal friction. A\
                    quickdraw consists of two non-locking carabiners connected\
                    together by a short, pre-sewn loop of webbing.",
                   updated=datetime.datetime.now(),
                   categories=category3)
db_session.add(climbItem2)
db_session.commit()

climbItem3 = Items(title="Harnesses",
                   description="A harness is a system used for connecting the\
                    rope to the climber. There are two loops at the front of\
                    the harness where the climber ties into the rope at the\
                    working end using a figure-eight knot]]. Most harnesses\
                    used in climbing are preconstructed and are worn around\
                    the pelvis and hips, although other types are used\
                    occasionally",
                   updated=datetime.datetime.now(),
                   categories=category3)
db_session.add(climbItem3)
db_session.commit()

climbItem4 = Items(title="Belay devices",
                   description="Belay devices are mechanical friction brake\
                    devices used to control a rope when belaying. Their main\
                    purpose is to allow the rope to be locked off with minimal\
                    effort to arrest a climber's fall.",
                   updated=datetime.datetime.now(),
                   categories=category3)
db_session.add(climbItem4)
db_session.commit()

climbItem5 = Items(title="Sling",
                   description="A sling or runner is an item of climbing\
                    equipment consisting of a tied or sewn loop of webbing\
                    that can be wrapped around sections of rock, hitched\
                    (tied) to other pieces of equipment or even tied directly\
                    to a tensioned line using a prusik knot, for anchor\
                    extension (to reduce rope drag and for other purposes),\
                    equalisation, or climbing the rope.",
                   updated=datetime.datetime.now(),
                   categories=category3)
db_session.add(climbItem5)
db_session.commit()


print "Sport items added."
