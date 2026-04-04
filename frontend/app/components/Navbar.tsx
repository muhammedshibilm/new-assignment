"use client";

import Link from "next/link";
import { usePathname, useRouter } from "next/navigation";
import { useEffect, useState } from "react";
import { getCurrentUser, logout } from "@/lib/auth";

export default function Navbar() {
  const pathname = usePathname();
  const router = useRouter();
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  useEffect(() => {
    let mounted = true;

    getCurrentUser().then((user) => {
      if (mounted) {
        setIsAuthenticated(Boolean(user));
      }
    });

    return () => {
      mounted = false;
    };
  }, [pathname]);

  const isAuthPage = pathname === "/login" || pathname === "/register";

  if (!isAuthenticated && isAuthPage) {
    return null;
  }

  async function handleLogout() {
    await logout();
    setIsAuthenticated(false);
    router.push("/login");
    router.refresh();
  }

  return (
    <nav className="flex items-center justify-between border-b px-6 py-3">
      <Link href="/" className="font-semibold">
        Dashboard
      </Link>
      <div className="flex items-center gap-3">
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
