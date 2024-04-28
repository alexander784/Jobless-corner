import React from 'react'
import "../App.css";

const Home = () => {
  return (
    <div className='welcome-container'>
      <div className='welcome'>

      
        <h2>Crabs Jobs</h2>

        <p className='mx-auto' style={{maxWidth:"600px"}}>

        Looking for your next career adventure? You're in the right place! Crab Jobs is your one-stop destination for discovering exciting job
         opportunities tailored just for you
         </p>

         </div>


 <div className="benefits-features">
  <div className='services'>
          <h3>Our Services</h3>
          <p>
          Create your profile and let data handle the rest
          <br/>
          We use advanced machine learning algorithms to match you and your future employer. Reduce the time spent on evaluating your potential and let us do it for you.


          </p>
          </div>
          <div className="ben-feat">
            <div className="work">
              <h5>HOw we Work </h5>
              <p>
              We have five simple steps to get you into you dream job, discover the process and be proud of the process.

              </p>
              <div className='how-work'>
                <p>
                We have five simple steps to get you into you dream job, discover the process and be proud of the process.

                </p>

              </div>
              <div className="feat">
              <h5>Features: </h5>
              <p>
                Add a Job
              </p>
            </div>
            </div>
            
          </div>
    </div>

    
          {/* <FOoter/> */}
    </div>


  )
}

export default Home;