import { createBrowserRouter } from "react-router-dom";
import MainLayout from "@/layouts/MainLayout";
import Dashboard from "@/pages/Dashboard";
import Repository from "@/pages/Repository";
import Graph from "@/pages/Graph";
import Simulation from "@/pages/Simulation";
import Prediction from "@/pages/Prediction";
import NotFound from "@/pages/NotFound";

export const router = createBrowserRouter([
  {
    path: "/",
    element: <MainLayout />,
    children: [
      { index: true, element: <Dashboard /> },
      { path: "repositories/:repoId", element: <Repository /> },
      { path: "repositories/:repoId/graph", element: <Graph /> },
      { path: "repositories/:repoId/simulation", element: <Simulation /> },
      { path: "repositories/:repoId/prediction", element: <Prediction /> },
    ],
  },
  { path: "*", element: <NotFound /> },
]);
