import React from 'react'
import Nav from '../components/Nav'
import Hero from '../components/Hero'
import QuickActions from '../components/QuickActions'
import Posts from '../components/Posts'

export default function Home() {
  return (
    <>
      <Nav />
      <QuickActions />
      <Hero />
      <Posts />
    </>
  )
}
