import React from 'react';
import { Link } from 'react-router-dom';
import Search from '../components/Layout/Search';
import News from '../assets/News.jpg';
import Smart from '../assets/Smart.avif';

const Home = () => {
  return (
    <div className='size-100 bg-gray-800'>
      <div className='flex justify-center items-center h-screen'>
        <p className='text-white text-6xl'>
          Meet the <span className='text-green-400'>Best</span> Tech <br /> Personality <br />
          to Grow Your Team
        </p>
        <div className='absolute bottom-0'>
          <Link to="/open-roles" className='container mx-5 rounded-3xl bg-slate-600 hover:bg-orange-950'>
            <button className=''>Open Role</button>
          </Link>
          <Link to="/PostRole" className='container mx-5 rounded-3xl bg-slate-600 hover:bg-orange-950'>
            <button className='button'>Post Role</button>
          </Link>
        </div>
      </div>
      <section className="container mx-auto px-6 p-10">
        <h2 className="text-4xl font-bold text-center text-white mb-8">
          Our services
        </h2>
        <div className="flex items-center flex-wrap mb-20">
          <div className="w-full md:w-1/2">
            <h4 className="text-3xl text-white font-bold mb-3">Exercise Metric</h4>
            <p className="text-gray-600 mb-8">
              Our Smart Health Monitoring Wristwatch is able to capture your vitals while you exercise. You can create different categories of exercises and can track your vitals on the go.
            </p>
          </div>
          <div className="w-full md:w-1/2">
            <img src={Smart} height={350} alt="Monitoring" />
          </div>
        </div>

        <div className="flex items-center flex-wrap mb-20">
          <div className="w-full md:w-1/2"></div>
          <div className="w-full md:w-1/2 pl-10">
            <h4 className="text-3xl text-white font-bold mb-3">How we work</h4>
            <p className="text-gray-600 mb-8">
              Our Smart Health Monitoring Wristwatch can generate a comprehensive report on your vitals depending on your settings either daily, weekly, monthly, quarterly, or yearly.
            </p>
            <img src={News} height={350} width={350} alt="Reporting" />
          </div>
        </div>
      </section>
    </div>
  );
};

export default Home;
