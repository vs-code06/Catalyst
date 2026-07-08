import { Outlet } from "react-router-dom";

// TODO: Add sidebar navigation, top bar, and notification system
export default function MainLayout() {
  return (
    <div className="flex h-screen bg-surface text-white">
      {/* Sidebar placeholder */}
      <aside className="w-64 bg-surface-secondary border-r border-surface-border" />
      {/* Main content */}
      <main className="flex-1 overflow-auto">
        <Outlet />
      </main>
    </div>
  );
}
