'use client';

import { useRouter } from 'next/navigation';
import { useEffect, useState } from 'react';
import { getCurrentUser } from '@/lib/auth';


export default function Dashboard() {
  const [user, setUser] = useState<{ user_id: number; role: string } | null>(null);
  const [checking, setChecking] = useState(true);
  const router = useRouter();

  useEffect(() => {
    let mounted = true;

    getCurrentUser().then((currentUser) => {
      if (!mounted) return;

      if (!currentUser) {
        router.replace('/login');
        return;
      }

      setUser(currentUser);
      setChecking(false);
    });

    return () => {
      mounted = false;
    };
  }, [router]);

  if (checking) {
    return <div className="p-6">Loading...</div>;
  }

  if (!user) {
    return null;
  }

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold">Welcome to Dashboard!</h1>
      <p className="mt-2 text-sm text-gray-600">Logged in as role: {user.role}</p>
    </div>
  );
}