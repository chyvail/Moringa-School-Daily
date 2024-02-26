import React from "react";
import Nav from "../components/Nav";
import QuickActions from "../components/QuickActions";
import Hero from "../components/Hero";
import Stats from "../components/Stats";
import UsersTable from "../components/UsersTable";
import PostsTable from "../components/PostsTable";

export default function Administration() {
  return (
    <>
      <Nav />
      <QuickActions />
      <Hero />
      <Stats />
      <hr className="mt-4" />
      <UsersTable />
      <hr className="mt-4" />
      <PostsTable />
    </>
  );
}
