import React, { useState, useEffect } from 'react'; // Importing useState and useEffect hooks from React
import BlogItem from "./BlogItem";

export default function BlogList(){
    const [blogs, setBlogs] = useState([]);
    const [userName, setUserName] = useState('');

    useEffect(()=>{
        fetch('http://localhost:5555/Content')
        .then(res=>res.json())
        .then(data=>setBlogs(data))
        .catch(error => console.error('Error fetching blog content:', error));
    },[])

    useEffect(() => {
        fetchUserData();
      }, []);

    const fetchUserData = () => {
        fetch('https://example.com/user')
          .then(res => res.json())
          .then(data => setUserName(data.firstName))
          .catch(error => console.error('Error fetching user data:', error));
      };

    return(
        <div className="container">
          <div className="row">
            <div className="col">
              <button className="btn btn-primary w-100">Add New Post</button> {/* Fixed class attribute */}
            </div>
          </div>
    
          <div className="row">
            <div className="col-lg-8 offset-lg-2">
              <div className="card mt-5">
                <div className="card-body">
                  <h3 className="card-title">Home.Blogs and New Content</h3>
                  <p className="card-subtitle mb-4">Indicator that one is in the home page</p>
    
                  <h1>Hello {userName}, Welcome to Moringa Daily</h1>
                  <p className="lead">Access authentic and verified information, inspiration, and advice about the tech space.</p>
                </div>
              </div>
            </div>
          </div> 
          {blogs.map((blog, index) => ( // Changed variable name from 'blogs' to 'blog'
            <BlogItem 
              key={index} 
              src={blog.urlToImage} 
              url={blog.url} 
              category={blog.category} 
              title={blog.title} 
              description={blog.description} 
              authorIcon="" 
              authorName=""
            />
          ))}
        </div>
    )
}
