import axios from "axios";

const API_BASE_URL = "http://localhost:8000"; // Your FastAPI backend URL

export async function fetchAllData() {
  const response = await axios.get(`${API_BASE_URL}/data/all`);
  return response.data;
}
