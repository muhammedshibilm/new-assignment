'use client';
import React, { useState } from 'react';
import { useRouter } from 'next/navigation';
import Link from 'next/link';
import { useEffect } from 'react';
import { getCurrentUser } from '@/lib/auth';

export default function LoginPage() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const router = useRouter();

  useEffect(() => {
    let mounted = true;

    getCurrentUser().then((user) => {
      if (mounted && user) {
        router.replace('/');
      }
    });

    return () => {
      mounted = false;
    };
  }, [router]);

  async function handleLogin(e : React.FormEvent<HTMLFormElement>) {
    e.preventDefault();
    
    const res = await fetch('http://localhost:8000/api/auth/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, password }),
      credentials: 'include',  // Important for cookie
    });

    if (res.ok) {
      router.push('/');  // Go to home page
    } else {
      setError('Wrong email or password');
    }
  }

  return (
      <div className='h-screen  flex items-center justify-center '>
     <div className='space-y-2'>
      <h1 className='text-3xl font-bold text-center'>Login</h1>
      <form onSubmit={handleLogin} className='space-y-2'>
        <input 
         className='border-2 rounded-lg py-2 px-1 '
          type="email" 
          placeholder="Email" 
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        /><br />
        <input 
        className='border-2 rounded-lg py-2 px-1 '
          type="password" 
          placeholder="Password" 
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        /><br />
        <button type="submit" className=' bg-white text-center w-full text-black  py-2 rounded-lg hover:cursor-pointer'>Login </button>
        <p className='text-xs text-center'>if don&apos;t have account <Link href={"/register"} className='text-gray-500'>Click here</Link> </p>
        {error && <p className='text-red-500'>{error}</p>}
      </form>
    </div>
      </div>
  );
}
