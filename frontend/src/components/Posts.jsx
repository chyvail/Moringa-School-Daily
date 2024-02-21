import React from 'react'
import Avatar from './Avatar'

export default function Posts() {
    const img_url = 'https://images.unsplash.com/photo-1498050108023-c5249f4df085?q=80&w=2944&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'
  return (
    <div className='container-lgs hero-top'>
        <p>All Blog Posts</p>
        <div className='row'>
            <div className='col-sm-4 blog-image'>
                <img src={img_url}/>
                <p className='mt-3'>Backend Development . <span>5 min read</span></p>
                <h4>Building the Backbone of the web</h4>
                <p className='post-description'>Analyze the evolving landscape of ransomware, recent trends, and proactive measures organizations can take to mitigate the risk of ransomware attacks.</p>
                <div className='custom-avatar'>
                    <Avatar height={40} alt="User Avatar" />
                </div>
            </div>
        </div>
    </div>
  )
}
