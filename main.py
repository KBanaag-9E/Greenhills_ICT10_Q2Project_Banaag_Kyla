from pyscript import display, document

# python function code for the Grade Calculator
def grade_calculator(e):
    document.getElementById('output').innerHTML = ""

    # gets full name of student
    fname = document.getElementById('firstName').value
    lname = document.getElementById('lastName').value
    name = f'{fname} {lname}'

    display(f'Student Name: {name}', target='output')

    # all subject variables
    sci = document.getElementById('s1').value
    eng = document.getElementById('s2').value
    fil = document.getElementById('s3').value
    math = document.getElementById('s4').value
    ss = document.getElementById('s5').value
    tle = document.getElementById('s6').value

    # displays subject scores
    display(f'Science: {sci}', target='output')
    display(f'English: {eng}', target='output')
    display(f'Filipino: {fil}', target='output')
    display(f'Mathematics: {math}', target='output')
    display(f'Philosophy: {ss}', target='output')
    display(f'TLE: {tle}', target='output')

    # assigns the default value of the subject input as 0 if no input is detected
    sci = int(("") or 0)
    eng = int(("") or 0)
    fil = int(("") or 0)
    math = int(("") or 0)
    ss = int(("") or 0)
    tle = int(("") or 0)

    subjects = [sci, eng, fil, math, ss, tle] # all subjecrs
    units = (5, 3, 2) # number of hours per subject

    # average weighted score
    final = round((float(subjects[0]) * units[0] +
        float(subjects[1]) * units[0] +
        float(subjects[2]) * units[1] +
        float(subjects[3]) * units[0] +
        float(subjects[4]) * units[1] +
        float(subjects[5]) * units[2]) / 
        (units[0] + units[0] + units[1] + units[0] + units[1] + units[2]), 2)

    display(f'Weighted Average: {final}', target='output')

# python function code for the Club Information
club_info = {
    "Math Club": {
        "Description": "Unlock the secrets within the formulas! Our Math Club is centered around creative problem-solving, fostering a passion for math and its applications in real-life scenarios through hands-on activities and collaborative projects.",
        "Meeting_Time": "Every Tuesday 2:30-3:30",
        "Location": "Room 701",
        "Moderator": "Mr. Mendoza",
        "Number_of_Members": 36
    }, 

    "Science Club": {
        "Description": "Uncover the universe's magic! Our Science Club offers students the opportunity to explore the world of science through a hands-on, experiential approach with lab experiments, field trips, and guest lectures from scientists and researchers. This club focuses on engaging students in various disciplines, including biology, chemistry, physics, and environmental science.",
        "Meeting_Time": "Every Thursday 2:30-3:30",
        "Location": "Room 510",
        "Moderator": "Mr. Bautista",
        "Number_of_Members": 28
    }, 

    "Robotics Club": {
        "Description": "Spark innovation and engineer the future! Our Robotics Club combines creativity with cutting-edge technology as students design, build, and program robots to solve real-world challenges. Through teamwork and hands-on projects, young innovators develop skills in coding, mechanical engineering, and problem-solving while preparing for competitive events.",
        "Meeting_Time": "Every Wednesday 2:30-4:30",
        "Location": "Room 704",
        "Moderator": "Ms. Torres",
        "Number_of_Members": 32
    },

    "Writing Club": {
        "Description": "Where words come alive! The Writing Club hones literary skills across genres—poetry, short stories, journalism, and more. Through workshops, peer reviews, and author visits, students refine their voice and technique. Some of our young authors will get to publish their works in the school literary magazine or compete in national writing contests.",
        "Meeting_Time": "Every Monday 2:30-3:30",
        "Location": "Room 511",
        "Moderator": "Mr. Rivera",
        "Number_of_Members": 36
    },

    "Art Club": {
        "Description": "Unleash your inner artist! Our Art Club nurtures self-expression through diverse mediums like painting, sculpture, digital art, and mixed media. Students explore techniques from classical to contemporary while developing their unique styles. Our activities include collaborative murals, gallery exhibitions, and cultural projects to celebrate creativity as a powerful tool for communication and change.",
        "Meeting_Time": "Every Friday 2:30-3:30",
        "Location": "Room 612",
        "Moderator": "Ms. Domingo",
        "Number_of_Members": 19
    },

    "Theater Club": {
        "Description": "Take center stage! The Theater Club ignites confidence and imagination through acting, stagecraft, and storytelling. From Shakespeare to original student-written plays, members engage in everything from set design to performance while learning voice projection, character development, and teamwork. We have annual productions showcase our young thespians’ talents to the school community.",
        "Meeting_Time": "Every Wednesday 2:30-4:30",
        "Location": "Room 701",
        "Moderator": "Ms. Lopez",
        "Number_of_Members": 22
    },
}

def any_club(e):
    document.getElementById("ClubInfo").innerText = ""
    club_name = document.getElementById("selected-club").value
    display(f"Description: {club_info[club_name]['Description']}", target='ClubInfo')
    display(f"Meeting Time: {club_info[club_name]['Meeting_Time']}", target='ClubInfo')
    display(f"Location: {club_info[club_name]['Location']}", target='ClubInfo')
    display(f"Club Moderator: {club_info[club_name]['Moderator']}", target='ClubInfo')
    display(f"Number of Members: {club_info[club_name]['Number_of_Members']}", target='ClubInfo')