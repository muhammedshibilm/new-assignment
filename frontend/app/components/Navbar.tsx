"use client";

import Link from "next/link";
import { usePathname, useRouter } from "next/navigation";
import { useEffect, useState } from "react";
import { getCurrentUser, logout, type SessionUser } from "@/lib/auth";

export default function Navbar() {
  const pathname = usePathname();
  const router = useRouter();
  const [user, setUser] = useState<SessionUser | null>(null);

  useEffect(() => {
    let mounted = true;

    getCurrentUser().then((user) => {
      if (mounted) {
        setUser(user);
      }
    });

    return () => {
      mounted = false;
    };
  }, [pathname]);

  const isAuthPage = pathname === "/login" || pathname === "/register";
  const isAuthenticated = Boolean(user);

  if (!isAuthenticated && isAuthPage) {
    return null;
  }

  async function handleLogout() {
    await logout();
    setUser(null);
    router.push("/login");
    router.refresh();
  }

  return (
    <nav className="flex items-center justify-between border-b px-6 py-3">
      <div className="flex items-center gap-4">
        <Link href="/" className="font-semibold">
          Dashboard
        </Link>
        {isAuthenticated && (
          <>
            <Link href="/task" className="text-sm text-gray-700">
              Task
            </Link>
            <Link href="/projects" className="text-sm text-gray-700">
              Projects
            </Link>
    
    
          </>
        )}
      </div>
      <div className="flex items-center gap-3">
                <div className="space-x-1.5 " >
                            <span>{user?.name}</span>
            {user?.role && (
              <span className="rounded-full border border-blue-300 bg-blue-50 px-2 py-1 text-xs font-medium text-blue-700">
               { user?.role}
              </span>
            )}
            </div>
        {isAuthenticated ? (
          <button
            onClick={handleLogout}
            className="rounded bg-black px-4 py-2 text-white hover:cursor-pointer"
          >
            Logout
          </button>
        ) : (
          <>
            <Link href="/login" className="text-sm text-gray-600">
              Login
            </Link>
            <Link href="/register" className="text-sm text-gray-600">
              Register
            </Link>
          </>
        )}
      </div>
    </nav>
  );
}
