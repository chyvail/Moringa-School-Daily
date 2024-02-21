import BlogItem from "./BlogItem";
import React, { useState, useEffect } from 'react';


export default function BlogList(){
    const [blogs, setBlogs] =useState([]);
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
              <button class="btn btn-primary w-100">Add New Post</button>
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
          {blogs.map((blogs,index)=>{
            return <BlogItem key = {index} src = {blogs.urlToImage} url = {blogs.url} category = {blogs.category} title = {blogs.title} description = {blogs.description} authorIcon="" authorName=""/>
          })}
        </div>
    )
}