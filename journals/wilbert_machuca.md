26 June 2023 : Started API endpoints designs. Researched models foreign key for relations between main models that are to be created. Design to show group the ideas for the model creation. Self explanatory but have to document that i have created my own journal within the team project to keep track of progress acquired.

27 June 2023: Today it was my round turn to share and do some typing into the issues for the project. As a team created all issues up to this point for the application. Issues where created on order of intended execution and by all team members approval. As a group came up with decision of using Postgres as our database moving forward since is one of the most required for modern development. We hooked up the PostgresDB and test it out from pgAdmin.

28 June 2023: As a team came to the decision of addressing the project without migration folder. Deleted the migrations and settled up the data and API > Queries folder accordingly. And we made the first steps of creating an User table, adding data to test it and baby steps the authorization. Pulled git repository up today and we all did our first git branch to tryout auth implementation.

11 July 2023: We created an DEV branch so we could use as group to develop the application. the plan is to merge in this branch while we are developing and then merge and launch the main branch for presentation.

12 July 2023: Team came up with a new diagram for the DDD. Adding a Seat showing model for the logic of reservation. I started the creation of the Booking Model. Wrote preliminary code without the real imports of the table relation ship since they are not done and working yet.

- Created booking table in the movies.sql(inside the data folder)
- Created bookings.py and code for the queries folder to handle the creation, get 1 and get all of the bookings.
- Created bookings.py and code for the routers folder to handle creation , get 1 and all for the booking api.

13 July 2023: Added confirmation code property for the booking table in the Database. This was made for the logic created in the bookings.py queries for automated creation of an 6 digit code when the booking is created. This is intended to be used in the event of sending an email to the user with the booking information and its Confirmation code to redeem at store.
I did not state it before but is never too late. I haven't made no migrations to test my table because its properties relationships hast been done to the point. Once those are created and working , the properties that are shared with the booking should be re-coded for perfect reference between them and test them.
Created Booking component with some preliminary code to fetch for the booking data and displayed using bootstrap. Created preliminary button to send the email and the code to handle that event. Needs to register the email provider and make the right connection to use the nodemailer.

17 July 2023: Fixed the queries BaseModel for teh Movie to handle the property of the image when we are using the model in the api and the front end. This had to be done to properly render the movie picture for each movie, which brings me with the creation of the movie detail react component that renders the movie title, description, picture. The card use in the bootstrap contains 3 buttons that are without any effect for the moment but should redirect to the given time for the movie in a certain room. This should let you pick the seats for that given time slot.

18 July 2023: Re wrote queries for the movies creation to handle the parse of the JSON object for the trailer. This was done for the creation of the Movie detail page to redirect to the Official YouTube video. Movie detail page contains a new "Watch Trailer" button. This was all handled by the front end react component and hooks. Created 2 Movie list components for user and admin to render the movie list with linkables titles. Links takes the user to the movie detail page. The admin list component allows the admin to delete a movie with a delete button. Added 4 Bar menu images to project, putted all images of project under picture folder and re routed all the endpoints using images. 4 images are used after clicking the Bar link in the Navbar frontend. Renders Bar Menu images in front end as cards.

24 July 2023: Finished rooms queries and routers calls to handle the post and the get 1 for to properly create rooms from FastAPI docs. Fixed queries/routers for showtimes to properly work. I will push this changes done to the showtimes in my own branch only for now and report it to team.

25 July 2023: Created email for the app purpose
gmail: javathescript10@gmail.com
password: MovieNight10
To be used in the email booking confirmation and contact us. Created component Contact.js to be render upon Navbar link "Contact". Shows Movie Night Logo and location information. Pages has the ability to auto open email sending form to the project email. Using react hooks and bootstrap buttons.
Played with the implementation of email sender, looks little challenging but should get there. Contact link and page working properly.

26 July 2023: Started day writing my first test_code. Using the Movies as the test since my booking model cant be implemented yet. Created a tests folder inside the API folder to handle files for test cases. Gave file name test_movies to handle the creation and get of Movies.Test code was deleted for now because the implementation is not that clear yet. I went ahead and worked with the Login.js and Signed Up components. They are rendering as expected and the Signup works well. Am not being able to login at the moment. I have implemented code in the Nav.js to show the logout button and its "HandleLogout" function in this file. I will be pushing work up to the point to my branch, API implementation for showtimes and seat should be done by today evening so I can concentrate in applying showtimes in the MovieDetails, and the booking confirmation page to render correct data.
Pulled from DEV to get latest changes from team mates up to the day. Worked on the merge to DEV with my updates and pushed it for every one to see. Deleted the homepage link and added its function to de Navbar main logo. When user clicks images gets sent to homepage.

27 July 2023: Merged into DEV as a Team to all of us have the latest changes. Re wrote Queries and Routers for bookings to be created correctly. Added SeatGenerator functionality to each of the TimeSlots instances for a Movie that has a showtime. Now every movie that has Showtimes buttons, its showtimes button auto render "seats/:showtime_id". Made Css changes to the Movie detail to proper render and scroll if overflow of display.

28 July 2023: Worked on final touches with what works, to be rendered correctly on DEV branch. Will be working for my last part as project is to create a Unit Test for Movies and Bookings.
