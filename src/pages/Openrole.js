import React from 'react';

const OpenRole = ({ roles }) => {

  return (
    <div className="container mx-auto px-6 p-10">
      <h2 className="text-4xl font-bold text-center text-gray-800 mb-8">
        Open Roles
      </h2>
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-8">
        {
         roles.map((role, index) => (
          <div key={index}
            className="bg-white shadow-md rounded-lg p-6">
            <h3 className="text-lg font-semibold text-gray-800">{role.roleName}</h3>
            <p className="text-sm text-gray-600 mt-2">{role.description}</p>
            <p className="text-sm text-gray-600 mt-2">Job Type: {role.jobType}</p>
            <p className="text-sm text-gray-600 mt-2">Duration: {role.duration}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default OpenRole;
