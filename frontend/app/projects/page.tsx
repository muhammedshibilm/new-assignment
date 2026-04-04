"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { getCurrentUser } from "@/lib/auth";

export default function ProjectsPage() {
  const router = useRouter();
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    let mounted = true;

    getCurrentUser().then((user) => {
      if (!mounted) return;
      if (!user) {
        router.replace("/login");
        return;
      }
      setLoading(false);
    });

    return () => {
      mounted = false;
    };
  }, [router]);

  if (loading) {
    return <div className="p-6">Loading...</div>;
  }

  return (
    <main className="p-6">
      <h1 className="text-2xl font-bold">Projects Page</h1>
      <p className="mt-2 text-gray-600">This is the /projects route.</p>
    </main>
  );
}
