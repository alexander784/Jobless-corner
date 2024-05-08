import React from 'react'
// import "../App.css";
import { Link } from 'react-router-dom';
import Search from '../components/Layout/Search';
import News from "../assets/News.jpg";
import Smart from "../assets/Smart.avif";
import sync from "../assets/sync.png";

const Home = () => {
  return (
    <div className='size-100 bg-gray-800'>
      <div className='flex justify-center items-center h-screen'>
        <div className='absolute top- bg-gray-200 p-5 rounded-lg text-center'>
        <p className='text-gray-800'>
        Looking for your next career adventure? You're in the right place! Crab Jobs is your one-stop destination for discovering exciting job
         opportunities tailored just for you
         </p>
         </div>
         <Search />
         
         <div className='absolute bottom-0'>
         <Link to="/open-roles" className='container mx-5 rounded-3xl bg-slate-600 hover:bg-orange-950'>
          <button className=''>open Role</button>
         </Link>
         <Link to="/post-roles" className='container mx-5 rounded-3xl bg-slate-600 hover:bg-orange-950'>
          <button className='button'>Post Role</button>
         </Link>
         </div>
         </div>
         <section class="container mx-auto px-6 p-10">
      <h2 class="text-4xl font-bold text-center text-gray-800 mb-8">
        Features
      </h2>
      <div class="flex items-center flex-wrap mb-20">
        <div class="w-full md:w-1/2">
          <h4 class="text-3xl text-gray-800 font-bold mb-3">Exercise Metric</h4>
          <p class="text-gray-600 mb-8">Our Smart Health Monitoring Wristwatch is able to capture you vitals while you exercise. You can create different category of exercises and can track your vitals on the go.</p>
        </div>
        <div class="w-full md:w-1/2">
          <img src={Smart} height={350} alt="Monitoring" />
        </div>
      </div>

      <div class="flex items-center flex-wrap mb-20">
        <div class="w-full md:w-1/2">
        </div>
        <div class="w-full md:w-1/2 pl-10">
          <h4 class="text-3xl text-gray-800 font-bold mb-3">Reporting</h4>
          <p class="text-gray-600 mb-8">Our Smart Health Monitoring Wristwatch can generate a comprehensive report on your vitals depending on your settings either daily, weekly, monthly, quarterly or yearly.</p>
          <img src={News} height={350} width={350}alt="Reporting" />

        </div>
      </div>

      <div class="flex items-center flex-wrap mb-20">
        <div class="w-full md:w-1/2">
          <h4 class="text-3xl text-gray-800 font-bold mb-3">Syncing</h4>
          <p class="text-gray-600 mb-8">Our Smart Health Monitoring Wristwatch allows you to sync data across all your mobile devices whether iOS, Android or Windows OS and also to your laptop whether MacOS, GNU/Linux or Windows OS.</p>
        </div>
        <div class="w-full md:w-1/2">
          <img src={sync} alt="Syncing" />
        </div>
      </div>
    </section>



 
             

    
          {/* <Footer/> */}
    </div>


  )
}

export default Home;