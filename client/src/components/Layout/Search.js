import React from 'react'

const Search = () => {
  return (
    <div className='absolute bottom-1 m-5'>
      <form>
        <input type='text' name='search' placeholder='search for job..' />
        <button type='submit'></button>
        </form>

    </div>
  )
}

export default Search;