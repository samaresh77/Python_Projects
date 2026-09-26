import { Box } from "@mui/material";
// import Sidebar from "./components/Sidebar";
// import Navbar from "./components/Navbar";
// import Dashboard from "./pages/Dashboard";

function App() {
  return (
    <Box>
      {/* <Sidebar /> */}

      {/* <Navbar /> */}

      <Box
        component="main"
        sx={{
          marginLeft: "240px",
          paddingTop: "90px",
          paddingX: 4,
          minHeight: "100vh",
          backgroundColor: "#f5f7fa",
        }}
      >
        {/* <Dashboard /> */}
      </Box>
    </Box>
  );
}

export default App;