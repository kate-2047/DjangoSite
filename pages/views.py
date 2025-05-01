from django.shortcuts import render

def home(request):
    return render(request, "pages/home.html")

def about(request):
    team = {
        'about' : [
            "Towne Engineering has provided Mechanical and Electrical Engineering Consulting throughout Upstate New York since 1975. Located in a mid-sized community in the beautiful Mohawk Valley, the firm is housed in a large circa 1860 Victorian home that has been restored in keeping with its age and architecture while adapting to the contemporary business requirements.",
            "Services include feasibility studies, design and development, preparation of bidding documents, and construction administration for new and retrofit commercial, government, industrial, and institutional projects.",
            "Since its inception, Towne Engineering has taken pride in consistently providing personalized, customized engineering services combined with traditional business principles and state-of-the-art technology."
        ],
        'member' : [
            {'name': 'William H. Towne', 
             'role': 'Founder', 
             'about': 'William H. Towne founded Towne Engineering in 1975. William earned his degree in Mechanical '
                'Engineering at Iowa State University and is a registered Professional '
                'Engineer in New York, Pennsylvania, Vermont, Wisconsin and Illinois. He holds'
                ' memberships in the American Society of Heating, Ventilating and Air '
                'Conditioning Engineers (ASHRAE) and the National Society of Professional '
                'Engineers (NSPE). The company has gone on the complete more than 4,000 projects under his supervision.',
            'photo': 'image/GuyOnATrain.JPG'},
           
            {'name': 'Christopher D. Krecidlo', 
             'role': 'Vice President', 
             'about': 'Christopher D. Krecidlo became a staff member in 2003, shortly after obtaining his '
                'Mechanical Engineering degree from State University of New York Institute '
                'of Technology and is a registered Professional Engineer in New York. His '
                'responsibility is mechanical systems design including heating, ventilating, '
                'air conditioning, plumbing and fire protection. He is a LEED Green Associate, '
                'a member of the American Society of Plumbing Engineers (ASPE), National '
                'Fire Protection Association (NFPA) and American Society of Health Care '
                'Engineers (ASHE).', 
             'photo': 'image/vp_headshot.JPG'},
        ]
    }
    return render(request, "pages/about.html", {'team': team})

def projects(request):
    portfolio = {
        'about' : [
        " Towne Engineering personnel have successfully completed the design and specification "
        "of Mechanical and Electrical Systems for more than 4000 projects associated with public "
        "schools, universities, libraries, nursing homes, hospitals, government buildings, residences, "
        "military installations, airport terminals, office buildings, banks, supermarkets, garages, "
        "and a large range of industrial facilities."
        ],
        'project' : [
            {'name': 'Rome Hospital',  
            'about': 'Construction of a new building-wide Energy Center, Rome Hospital, Rome NY',
            'photo': 'image/EnergyCenter.jpg'},
        
            {'name': 'Mohawk Valley Community College', 
            'about': 'Exterior lighting upgrade and retrofit, MVCC Payne Hall, Utica NY', 
            'photo': 'image/PayneHallSign2.jpg'},

            {'name': 'Oneida County Parking Garage', 
            'about': 'Design and construction administration of snowmelt system, Oneida County Pakring '
            'Garage Helipad, Utica NY' , 
            'photo': 'image/Helipad.jpg'},

            {'name': 'WestRock Chiller Plant', 
            'about': 'WestRock Paperboard Mill Chiller Plant replacement and retrofit, Solvay NY', 
            'photo': 'image/ChillerPlant.png'},
        
            {'name': 'Union Station', 
            'about': 'Boiler room retrofit, Utica NY', 
            'photo': 'image/unionstation.jpg'},
        ]
    }
    return render(request, "pages/projects.html", {'portfolio': portfolio})

def contactus(request):
    return render(request, "pages/contactus.html")