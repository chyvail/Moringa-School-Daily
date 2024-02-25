import React from "react";
import Nav from "../components/Nav";
import QuickActions from "../components/QuickActions";
import Hero from "../components/Hero";
import Stats from "../components/Stats";
import UsersTable from "../components/UsersTable";

export default function Administration() {
  return (
    <>
      <Nav />
      <QuickActions />
      <Hero />
      <Stats />
      <UsersTable />
    </>
  );
}
