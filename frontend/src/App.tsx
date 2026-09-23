import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { Login } from './pages/auth/Login';
import { DashboardLayout } from './layouts/DashboardLayout';
import { ProtectedRoute } from './components/ProtectedRoute';
import { useAuthStore } from './store/authStore';

// Temporary dummy components for roles
const StudentDashboard = () => <div>Student Dashboard Content</div>;
const StaffDashboard = () => <div>Staff Dashboard Content</div>;
const HodDashboard = () => <div>HOD Dashboard Content</div>;
const AdminDashboard = () => <div>Admin Dashboard Content</div>;
const Unauthorized = () => <div>Unauthorized Access</div>;

function App() {
  const { user } = useAuthStore();

  const getDashboardPath = () => {
    if (!user) return '/login';
    switch (user.role) {
      case 'ADMIN': return '/admin';
      case 'HOD': return '/hod';
      case 'STAFF': return '/staff';
      case 'STUDENT': return '/student';
      default: return '/login';
    }
  };

  return (
    <Router>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/unauthorized" element={<Unauthorized />} />
        
        {/* Redirect root to appropriate dashboard */}
        <Route path="/" element={<Navigate to={getDashboardPath()} replace />} />

        {/* Protected Routes Wrapper */}
        <Route element={<DashboardLayout />}>
          
          <Route element={<ProtectedRoute allowedRoles={['STUDENT']} />}>
            <Route path="/student" element={<StudentDashboard />} />
          </Route>
          
          <Route element={<ProtectedRoute allowedRoles={['STAFF']} />}>
            <Route path="/staff" element={<StaffDashboard />} />
          </Route>
          
          <Route element={<ProtectedRoute allowedRoles={['HOD']} />}>
            <Route path="/hod" element={<HodDashboard />} />
          </Route>
          
          <Route element={<ProtectedRoute allowedRoles={['ADMIN']} />}>
            <Route path="/admin" element={<AdminDashboard />} />
          </Route>

        </Route>
      </Routes>
    </Router>
  );
}

export default App;
